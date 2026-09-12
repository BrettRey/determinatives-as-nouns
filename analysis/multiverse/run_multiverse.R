#!/usr/bin/env Rscript
# Exploratory reanalysis of a fixed, hand-coded inventory. No taxonomic-rank test.
# Run from anywhere: R_LIBS_USER=/tmp/determinatives-Rlib Rscript <this file>
# Optional first argument: a separate output directory for a verification replay.
suppressPackageStartupMessages({
  library(cluster)
  library(energy)
  library(digest)
})
options(stringsAsFactors=FALSE)
argv <- commandArgs(trailingOnly=FALSE)
script <- sub("^--file=", "", argv[grepl("^--file=", argv)])
root <- dirname(normalizePath(script))
extra <- commandArgs(trailingOnly=TRUE)
out <- if(length(extra)) extra[1] else file.path(root, "results")
dir.create(out, recursive=TRUE, showWarnings=FALSE)
save_csv <- function(x, name) write.csv(x, file.path(out, name), row.names=FALSE, na="")

raw <- read.csv(file.path(root, "../data/matrix155-lingbuzz.csv"), check.names=FALSE)
stopifnot(nrow(raw)==138, ncol(raw)==156,
          all(as.matrix(raw[,-1]) %in% c("y","n")),
          !anyDuplicated(raw[[1]]))
X <- matrix(as.integer(as.matrix(raw[,-1])=="y"), nrow=138,
            dimnames=list(raw[[1]], names(raw)[-1]))
blocks <- read.csv(file.path(root, "data/feature-blocks.csv"))
stopifnot(identical(blocks$feature, colnames(X)),
          identical(as.integer(table(factor(blocks$block,
                    levels=c("morph","phon","sem","synt")))), c(66L,3L,36L,50L)))
stopifnot(digest(file=file.path(root, "../data/matrix155-lingbuzz.csv"),
                 algo="sha256") ==
          "a15af082a6bc5dbe24bcf57475c35cad1b00c2dc7e17af584db1841bf7abddf7")
items <- rownames(X)
reference <- c(rep(1L,73), rep(2L,65))
analysis_labels <- c("functions_as_fused_determiner_head",
                     "functions_as_head_of_partitive_construction",
                     "functions_as_subject_determiner",
                     "May_coordinate_with_non_fused_determiners")
is_label <- colnames(X) %in% analysis_labels
is_component <- seq_len(ncol(X)) <= 50
block <- setNames(blocks$block, blocks$feature)
features <- transform(blocks, word_component=is_component, explicit_analysis_label=is_label,
                      present_count=colSums(X),
                      profile_id=match(apply(X,2,paste0,collapse=""),
                                       unique(apply(X,2,paste0,collapse=""))))
save_csv(features, "feature-inventory.csv")
save_csv(data.frame(word=items, reference=reference,
                    reference_class=c(rep("determinative",73),rep("pronoun",65))),
         "item-inventory.csv")

ari <- function(a,b) {
  tab <- table(a,b); n2 <- choose(sum(tab),2)
  ab <- sum(choose(tab,2)); aa <- sum(choose(rowSums(tab),2))
  bb <- sum(choose(colSums(tab),2)); expected <- aa*bb/n2
  denom <- (aa+bb)/2-expected
  if(abs(denom)<1e-14) return(if(identical(outer(a,a,"=="),outer(b,b,"=="))) 1 else 0)
  (ab-expected)/denom
}
orient <- function(cl) {
  if(sum(cl==reference)<length(reference)/2) cl <- 3L-cl
  as.integer(cl)
}
agreement <- function(cl) max(sum(cl==reference),sum(cl!=reference))
sil <- function(cl,D) mean(cluster::silhouette(cl, as.dist(D))[,"sil_width"])

weight_vector <- function(z, mode) {
  w <- switch(mode,
    equal_features=rep(1,ncol(z)),
    equal_domains={
      b <- block[colnames(z)]
      1/as.numeric(table(b)[b])
    },
    unique_profiles={
      key <- apply(z,2,paste0,collapse="")
      1/as.numeric(table(key)[key])
    },
    idf_presence=log(nrow(z)/pmax(1,colSums(z))),
    stop("Unknown weighting"))
  stopifnot(all(is.finite(w)), all(w>=0), sum(w)>0)
  w/sum(w)
}
distance_matrix <- function(z,w,metric) {
  # Binary x^2=x: use weighted intersections to compute exact mismatch sums.
  zw <- sweep(z,2,w,"*")
  shared <- tcrossprod(zw,z)
  present <- rowSums(zw)
  mismatch <- outer(present,present,"+")-2*shared
  mismatch[mismatch<1e-14] <- 0
  D <- switch(metric,
    hamming=mismatch,
    sqrt_hamming=sqrt(mismatch),
    jaccard={
      union <- outer(present,present,"+")-shared
      d <- matrix(0,nrow(z),nrow(z))
      valid <- union>1e-14
      d[valid] <- mismatch[valid]/union[valid]
      d
    }, stop("Unknown distance"))
  D <- (D+t(D))/2
  diag(D) <- 0
  dimnames(D) <- list(rownames(z),rownames(z))
  stopifnot(all(is.finite(D)),min(D)>=-1e-12,max(D)<=1+1e-10)
  D
}
# Geometrically identical choices within a feature set are aliases, not extra votes.
geometry_grid <- function(z) {
  ans <- list(); aliases <- list(); seen <- character()
  for(wm in c("equal_features","equal_domains","unique_profiles","idf_presence")) {
    w <- weight_vector(z,wm)
    for(dm in if(wm=="idf_presence") "jaccard" else c("sqrt_hamming","hamming","jaccard")) {
      D <- distance_matrix(z,w,dm)
      # Retain the metric name: energy is used only on Euclidean sqrt-mismatch.
      key <- paste(dm,digest(round(unname(D),12),algo="sha256"))
      if(key %in% seen) {
        aliases[[length(aliases)+1L]] <- data.frame(weight=wm,distance=dm,
          canonical_weight=ans[[match(key,seen)]]$weight)
      } else {
        seen <- c(seen,key)
        ans[[length(ans)+1L]] <- list(weight=wm,distance=dm,D=D,w=w)
      }
    }
  }
  list(geometries=ans,aliases=aliases)
}

all_idx <- seq_len(ncol(X))
sets <- list(full=all_idx,
  no_components=which(!is_component),
  no_four_labels=which(!is_label),
  no_components_or_four_labels=which(!is_component & !is_label),
  no_morph=which(block!="morph"),
  no_phon=which(block!="phon"),
  no_sem=which(block!="sem"),
  no_synt=which(block!="synt"),
  morph_only=which(block=="morph"),
  morph_without_components=which(block=="morph" & !is_component),
  phon_only=which(block=="phon"),
  sem_only=which(block=="sem"),
  synt_only=which(block=="synt"),
  synt_without_four_labels=which(block=="synt" & !is_label))
core_names <- names(sets)[1:8]
set_membership <- do.call(rbind,lapply(names(sets),function(nm) {
  data.frame(feature_set=nm,scope=if(nm %in% core_names) "core" else "domain_diagnostic",
             feature=colnames(X)[sets[[nm]]])
}))
save_csv(set_membership, "feature-sets.csv")

start_rows <- list()
fit_two <- function(D,method,id) {
  if(method=="pam") {
    f <- cluster::pam(as.dist(D),2,diss=TRUE,variant="original",
                      keep.diss=FALSE,keep.data=FALSE)
    return(list(cluster=as.integer(f$clustering),objective=unname(f$objective[2]),
                starts=1L,iterations=NA_integer_,tied_best_partitions=1L,
                converged=TRUE))
  }
  if(method=="average") {
    cl <- cutree(hclust(as.dist(D),method="average"),2)
    return(list(cluster=as.integer(cl),objective=NA_real_,starts=1L,
                iterations=NA_integer_,tied_best_partitions=1L,converged=TRUE))
  }
  fits <- lapply(1:100,function(seed) {
    set.seed(seed)
    energy::kgroups(as.dist(D),2,iter.max=100,nstart=1)
  })
  objectives <- vapply(fits,function(f) f$W,numeric(1))
  best <- which.min(objectives)
  winner <- fits[[best]]
  near <- which(abs(objectives-min(objectives))<1e-10)
  partition_keys <- vapply(fits,function(f) paste(orient(f$cluster),collapse=""),character(1))
  start_rows[[length(start_rows)+1L]] <<- data.frame(
    fit_id=id,seed=1:100,objective=objectives,
    matched=vapply(fits,function(f) agreement(f$cluster),numeric(1)),
    ari=vapply(fits,function(f) ari(f$cluster,reference),numeric(1)),
    iterations=vapply(fits,function(f) f$iterations,numeric(1)),
    last_moves=vapply(fits,function(f) f$count,numeric(1)),
    selected=seq_along(fits)==best)
  list(cluster=as.integer(winner$cluster),objective=winner$W,starts=100L,
       iterations=winner$iterations,
       tied_best_partitions=length(unique(partition_keys[near])),
       converged=!(winner$iterations==100 && winner$count>0))
}

spec_rows <- assignment_rows <- k_rows <- alias_rows <- weight_rows <- list()
spec_count <- 0L
for(nm in names(sets)) {
  z <- X[,sets[[nm]],drop=FALSE]
  scope <- if(nm %in% core_names) "core" else "domain_diagnostic"
  grid <- geometry_grid(z)
  for(a in grid$aliases)
    alias_rows[[length(alias_rows)+1L]] <- cbind(feature_set=nm,a)
  # Don't force k beyond the number of observed binary profiles.
  max_k <- min(8L,nrow(unique(z)))
  for(g in grid$geometries) {
    D <- g$D
    geometry_id <- paste(nm,g$weight,g$distance,sep="__")
    weight_rows[[length(weight_rows)+1L]] <- data.frame(
      geometry_id=geometry_id,feature=colnames(z),weight=g$w)
    methods <- c("pam","average",if(g$distance=="sqrt_hamming") "energy")
    for(method in methods) {
      id <- paste(geometry_id,method,sep="__")
      fit <- fit_two(D,method,id)
      cl <- orient(fit$cluster)
      spec_count <- spec_count+1L
      row <- data.frame(spec_id=id,scope=scope,feature_set=nm,features=ncol(z),
        weighting=g$weight,distance=g$distance,method=method,k=2L,
        matched=agreement(cl),total=length(cl),ari=ari(cl,reference),
        balanced_accuracy=mean(c(mean(cl[reference==1]==1),mean(cl[reference==2]==2))),
        orientation_tied=agreement(cl)==69,
        size_1=sum(cl==1),size_2=sum(cl==2),
        silhouette=sil(cl,D),objective=fit$objective,starts=fit$starts,
        iterations=fit$iterations,tied_best_partitions=fit$tied_best_partitions,
        converged=fit$converged)
      spec_rows[[spec_count]] <- row
      assignment_rows[[spec_count]] <- data.frame(spec_id=id,word=items,
                                                 reference=reference,cluster=cl)
      if(method!="energy") {
        tree <- if(method=="average") hclust(as.dist(D),method="average") else NULL
        for(k in 2:max_k) {
          kc <- if(k==2) cl else if(method=="average") cutree(tree,k) else
            cluster::pam(as.dist(D),k,diss=TRUE,variant="original",cluster.only=TRUE)
          k_rows[[length(k_rows)+1L]] <- data.frame(spec_id=id,scope=scope,
            feature_set=nm,weighting=g$weight,distance=g$distance,method=method,
            k=k,max_k_examined=max_k,silhouette=sil(kc,D),ari=ari(kc,reference))
        }
      }
    }
  }
  cat(sprintf("Clustering: %-31s %3d cumulative two-group specifications\n",nm,spec_count))
  flush.console()
}
specs <- do.call(rbind,spec_rows)
assignments <- do.call(rbind,assignment_rows)
save_csv(specs,"specifications.csv")
save_csv(assignments,"assignments.csv")
save_csv(do.call(rbind,k_rows),"k-sensitivity.csv")
save_csv(do.call(rbind,alias_rows),"equivalent-choices.csv")
save_csv(do.call(rbind,weight_rows),"feature-weights.csv")

# Coassignment has no orientation ambiguity. Summaries are conditional on this menu,
# not posterior probabilities of category membership or independent replications.
for(method in unique(specs$method)) {
  keep <- specs$spec_id[specs$scope=="core" & specs$method==method]
  labels <- sapply(keep,function(id) assignments$cluster[assignments$spec_id==id])
  co <- Reduce("+",lapply(seq_len(ncol(labels)),
              function(j) outer(labels[,j],labels[,j],"==")))/ncol(labels)
  # Set transparent column names after data.frame's automatic matrix expansion.
  co_df <- data.frame(word=items,co,check.names=FALSE)
  names(co_df) <- c("word",items)
  save_csv(co_df,paste0("coassignment-core-",method,".csv"))
  valid_ids <- keep[!specs$orientation_tied[match(keep,specs$spec_id)]]
  aligned <- sapply(valid_ids,function(id) assignments$cluster[assignments$spec_id==id])
  save_csv(data.frame(word=items,reference=reference,specifications=length(valid_ids),
    excluded_orientation_ties=length(keep)-length(valid_ids),
    determinative_aligned_count=rowSums(aligned==1),
    pronoun_aligned_count=rowSums(aligned==2),
    agreement_count=rowSums(aligned==reference)),
    paste0("membership-core-",method,".csv"))
}

# Withhold an entire domain before computing distances or clusters.
# Also remove train columns identical/complementary to any held-out column.
# Estimate held-out Bernoulli rates from other rows in the same group, using
# Beta(1,1) smoothing; the target row never estimates its own held-out rate.
# This is transductive transfer within this inventory, not new-lexeme validation.
loo_rates <- function(y,cl) {
  p <- matrix(NA_real_,nrow(y),ncol(y),dimnames=dimnames(y))
  for(group in unique(cl)) {
    idx <- which(cl==group)
    totals <- colSums(y[idx,,drop=FALSE])
    p[idx,] <- (matrix(totals+1,nrow=length(idx),ncol=ncol(y),byrow=TRUE) -
               y[idx,,drop=FALSE])/(length(idx)+1)
  }
  p
}
loss <- function(y,p) -(y*log(p)+(1-y)*log1p(-p))
prediction_rows <- prediction_feature_rows <- prediction_item_rows <- list()
prediction_assignments <- prediction_schema <- prediction_aliases <- list()
for(held_domain in c("morph","phon","sem","synt")) {
  for(coding in c("all_features","omit_four_labels")) {
    eligible <- if(coding=="all_features") rep(TRUE,ncol(X)) else !is_label
    target <- which(block==held_domain & eligible)
    train <- which(block!=held_domain & eligible)
    y <- X[,target,drop=FALSE]
    target_keys <- c(apply(y,2,paste0,collapse=""),apply(1-y,2,paste0,collapse=""))
    blocked <- train[apply(X[,train,drop=FALSE],2,paste0,collapse="") %in% target_keys]
    train <- setdiff(train,blocked)
    z <- X[,train,drop=FALSE]
    fold_id <- paste(held_domain,coding,sep="__")
    prediction_schema[[length(prediction_schema)+1L]] <- data.frame(
      fold_id=fold_id,feature=colnames(X),
      role=ifelse(seq_len(ncol(X)) %in% target,"target",
        ifelse(seq_len(ncol(X)) %in% train,"train",
          ifelse(seq_len(ncol(X)) %in% blocked,"duplicate_or_complement","omitted_label"))))
    baseline_p <- loo_rates(y,rep(1L,nrow(y)))
    reference_p <- loo_rates(y,reference)
    baseline_loss <- loss(y,baseline_p)
    reference_loss <- loss(y,reference_p)
    pg <- geometry_grid(z)
    for(a in pg$aliases)
      prediction_aliases[[length(prediction_aliases)+1L]] <- cbind(fold_id=fold_id,a)
    for(g in pg$geometries) {
      for(method in c("pam","average",if(g$distance=="sqrt_hamming") "energy")) {
        id <- paste("predict",fold_id,g$weight,g$distance,method,sep="__")
        fit <- fit_two(g$D,method,id)
        cl <- orient(fit$cluster)
        p <- loo_rates(y,cl)
        model_loss <- loss(y,p)
        gain <- baseline_loss-model_loss
        vs_reference <- reference_loss-model_loss
        prediction_rows[[length(prediction_rows)+1L]] <- data.frame(
          prediction_id=id,held_domain=held_domain,coding=coding,
          training_features=length(train),held_features=length(target),
          blocked_duplicate_columns=length(blocked),
          weighting=g$weight,distance=g$distance,method=method,
          cells=length(y),cluster_logloss=mean(model_loss),
          baseline_logloss=mean(baseline_loss),reference_logloss=mean(reference_loss),
          gain_over_baseline=mean(gain),gain_over_reference=mean(vs_reference),
          cluster_brier=mean((y-p)^2),baseline_brier=mean((y-baseline_p)^2),
          reference_brier=mean((y-reference_p)^2),converged=fit$converged)
        prediction_feature_rows[[length(prediction_feature_rows)+1L]] <- data.frame(
          prediction_id=id,feature=colnames(y),cluster_logloss=colMeans(model_loss),
          baseline_logloss=colMeans(baseline_loss),reference_logloss=colMeans(reference_loss),
          gain_over_baseline=colMeans(gain),gain_over_reference=colMeans(vs_reference))
        prediction_item_rows[[length(prediction_item_rows)+1L]] <- data.frame(
          prediction_id=id,word=items,cluster_logloss=rowMeans(model_loss),
          baseline_logloss=rowMeans(baseline_loss),reference_logloss=rowMeans(reference_loss),
          gain_over_baseline=rowMeans(gain),gain_over_reference=rowMeans(vs_reference))
        prediction_assignments[[length(prediction_assignments)+1L]] <- data.frame(
          prediction_id=id,word=items,cluster=cl)
      }
    }
    cat(sprintf("Prediction: %s; %d training, %d held features, %d duplicate/complement exclusions\n",
                fold_id,length(train),length(target),length(blocked)))
    flush.console()
  }
}
save_csv(do.call(rbind,prediction_rows),"held-domain-prediction.csv")
save_csv(do.call(rbind,prediction_feature_rows),"prediction-by-feature.csv")
save_csv(do.call(rbind,prediction_item_rows),"prediction-by-item.csv")
save_csv(do.call(rbind,prediction_assignments),"prediction-assignments.csv")
save_csv(do.call(rbind,prediction_schema),"prediction-folds.csv")
save_csv(do.call(rbind,prediction_aliases),"prediction-equivalent-choices.csv")
save_csv(do.call(rbind,start_rows),"energy-starts.csv")

# Direct control against the existing audit's original coordinate implementation.
set.seed(20260907)
legacy <- energy::kgroups(X,2,iter.max=100,nstart=100)
legacy_obj <- sum(vapply(split(seq_len(nrow(X)),legacy$cluster),function(idx)
                  sum(as.matrix(dist(X))[idx,idx])/(2*length(idx)),numeric(1)))
stopifnot(abs(legacy_obj-legacy$W)<1e-8)
legacy_row <- data.frame(seed=20260907,features=155,matched=agreement(legacy$cluster),
                         objective=legacy$W,independently_recomputed_objective=legacy_obj)
save_csv(legacy_row,"legacy-control.csv")
save_csv(data.frame(word=items,cluster=orient(legacy$cluster)),"legacy-control-assignments.csv")
writeLines(c("Exploratory fixed-matrix analysis; source and limits in PROTOCOL.txt.",
             "Random starts: energy seeds 1:100, iter.max=100; winner minimizes W.",
             "PAM uses deterministic original BUILD/SWAP; average linkage is deterministic.",
             "Legacy control: seed 20260907, nstart=100, iter.max=100, unscaled X.",
             capture.output(sessionInfo())),file.path(out,"R-session-info.txt"))
cat(sprintf("Finished: %d two-group specifications; %d domain-transfer fits.\n",
            nrow(specs),length(prediction_rows)))
