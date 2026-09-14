# Lexeme/construction record extraction

Follow `system-prompt.txt` and perform the complete extraction task in `prompt.json`, using only its supplied manuscript excerpts. The same schema and source excerpts are also provided separately in `schema.json` and `sources.json` for convenience.

Deliver a file named `records.json` containing the requested JSON object: seven lexeme records, five construction records, 20 participation claims, and the two scope checks. Match the supplied schema exactly. Preserve the given query identifiers and the distinction between excluded and not stated. Evidence quotes must be exact source substrings. Do not introduce other sources or background linguistic facts.

This is a bounded source-extraction task. No Lean formalization or theorem proving is requested. Do not substitute a proof or a narrative report for the JSON deliverable. Do not edit the supplied source files. If unable to produce the records, explain that in a separate report rather than inventing content.
