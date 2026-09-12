#!/usr/bin/env Rscript
# Reproduction and sensitivity audit, not a test of taxonomic rank.
# Run after recover_matrix.py, with the energy package available.
library(energy)
args <- commandArgs(trailingOnly=FALSE)
script <- sub('^--file=', '', args[grepl('^--file=', args)])
root <- dirname(normalizePath(script))
out <- file.path(root, 'results')
dir.create(out, showWarnings=FALSE)
load_matrix <- function(name) {
  x <- read.csv(file.path(root, 'data', name), check.names=FALSE)
  z <- as.matrix(x[, -1])
  stopifnot(all(z %in% c('n', 'y')), nrow(z)==138)
  matrix(as.integer(z=='y'), nrow=nrow(z), dimnames=list(x[[1]], colnames(z)))
}
public <- load_matrix('matrix155-lingbuzz.csv')
working <- load_matrix('matrix232-recovered.csv')
syntax_start <- match('can_be_followed_by_adjective_such', colnames(public))
syntax <- public[, syntax_start:ncol(public)]
# A limited check of four explicit analysis labels; the remaining judgments
# are still largely CGEL-derived and are not theory-independent observations.
analysis_labels <- c('functions_as_fused_determiner_head',
                     'functions_as_head_of_partitive_construction',
                     'functions_as_subject_determiner',
                     'May_coordinate_with_non_fused_determiners')
variants <- list(public155=public,
                 appendix154=public[, -1],
                 working232=working,
                 working_appendix231=working[, -1],
                 no_word_component_columns=public[, 51:ncol(public)],
                 syntax50=syntax,
                 syntax_without_four_analysis_labels=syntax[, !colnames(syntax) %in% analysis_labels])
reference <- c(rep(1L, 73), rep(2L, 65))
agreement <- function(cl) {
  n <- sum(cl==reference)
  max(n, length(reference)-n)
}
single_runs <- list()
summaries <- list()
assignments <- list()
disco_results <- list()
for (name in names(variants)) {
  z <- variants[[name]]
  runs <- do.call(rbind, lapply(1:100, function(seed) {
    set.seed(seed)
    fit <- kgroups(z, 2, iter.max=10, nstart=1)
    data.frame(variant=name, features=ncol(z), seed=seed,
               matched=agreement(fit$cluster), total=138,
               objective=fit$W, iterations=fit$iterations)
  }))
  single_runs[[name]] <- runs
  set.seed(20260907)
  best <- kgroups(z, 2, iter.max=100, nstart=100)
  # Orient arbitrary cluster numbers by maximum match to the reference.
  cl <- best$cluster
  if (sum(cl==reference)<69) cl <- 3L-cl
  assignments[[name]] <- data.frame(variant=name,
      word=rownames(public), reference=reference, cluster=cl)
  summaries[[name]] <- data.frame(variant=name, features=ncol(z),
      single_start_min=min(runs$matched),
      single_start_median=median(runs$matched),
      single_start_max=max(runs$matched),
      single_start_equal_129=sum(runs$matched==129),
      best_of_100_matched=agreement(best$cluster), total=138,
      objective=best$W, iterations=best$iterations)
  set.seed(20260907)
  fit <- eqdist.etest(z, sizes=c(73,65), R=999, method='discoF')
  disco_results[[name]] <- data.frame(variant=name, features=ncol(z),
      between=unname(fit$between), within=unname(fit$within),
      total=unname(fit$total), df_between=unname(fit$Df.trt),
      df_within=unname(fit$Df.e), F=unname(fit$statistic),
      p=unname(fit$p.value), permutations=999)
}
write.csv(do.call(rbind, single_runs), file.path(out,'kgroups-single-starts.csv'), row.names=FALSE)
summary <- do.call(rbind, summaries)
write.csv(summary, file.path(out,'kgroups-summary.csv'), row.names=FALSE)
write.csv(do.call(rbind, assignments), file.path(out,'kgroups-assignments.csv'), row.names=FALSE)
disco <- do.call(rbind, disco_results)
write.csv(disco, file.path(out,'disco-sensitivity.csv'), row.names=FALSE)
# The published appendix splits determinatives; the prose calls the split
# pronouns. Report both as a provenance check without choosing a match.
split_results <- lapply(c('determinatives','pronouns'), function(group) {
  z <- if(group=='determinatives') public[1:73,] else public[74:138,]
  sizes <- if(group=='determinatives') c(35,38) else c(32,33)
  set.seed(20260907)
  fit <- eqdist.etest(z,sizes=sizes,R=999,method='discoF')
  data.frame(group=group,first=sizes[1],second=sizes[2],
             F=unname(fit$statistic),p=unname(fit$p.value))
})
write.csv(do.call(rbind,split_results),file.path(out,'within-category-splits.csv'),row.names=FALSE)
writeLines(c('Seed schedule: individual seeds 1:100; multi-start/DISCO seed 20260907.',
             'No common or proper nouns in this matrix: rank and nounhood are untested.',
             capture.output(sessionInfo())),file.path(out,'R-session-info.txt'))
print(summary, row.names=FALSE)
print(disco[,c('variant','F','p')], row.names=FALSE)
