# Expanded source-to-JSON extraction

Follow task.json using only the two complete source texts it supplies. Return records.json matching schema.json, and exceptions.json as an array of any unresolved items (each with query_id, reason, and source evidence); use [] when there are none. Preserve all IDs, exact source quotations, conditions, qualifications and scope distinctions. Do not replace the requested JSON with Lean work. You may write a concise extraction summary separately.
