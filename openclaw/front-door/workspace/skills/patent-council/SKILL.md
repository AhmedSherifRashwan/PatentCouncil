---
name: patent-council
description: Open, launch, monitor and deliver a Patent Council matter — an inventor's disclosure turned into a Patent Application and a Prosecution Assessment by the council's agents. Use whenever someone wants patent drafting, a patentability view, prior art or a filing package for an invention, wants to check on a run, or answers the inventor questions.
metadata:
  short-description: Run a Patent Council matter
---

# Patent Council — front-door skill

Turn a request into a matter run by the `council` runner. **The runner reports back into this conversation by
itself** as `[Patent Council update]` messages. You never poll, never wait, never promise to check later.

## Where things live

- Runner: `/Users/ahmed/PatentCouncil/tools/council <command>` (prints one JSON object; returns in seconds).
- A matter's dossier: `/Users/ahmed/PatentCouncil/matters/<slug>/` (`intake/` = what the person gave; `runs/r1/` = the run).
- The two documents: `matters/<slug>/runs/r1/package/readable/` (`.docx` and `.pdf` of each).
- The live ticker: `matters/<slug>/runs/r1/progress.md`.

Run every command with the exec tool, in the foreground, default timeout. Never run anything in the background
yourself: `--background` makes the runner detach on its own.

## Your session key

Every launch needs your own session key so the runner knows where to post updates. Get it from the
`session_status` tool (the `agent:patent-council:...` string) and pass it as `--notify <key>`.

## 1. Open a matter

Slug: short, lowercase, letters, digits and hyphens, plus the date (e.g. `smart-valve-20261001`). Ask for a title
only if none can be taken from what they said.

```bash
/Users/ahmed/PatentCouncil/tools/council new-matter --slug <slug> --title "<title>" --jurisdictions US,EP,GB --profile full
```

Add `--from-example` for the fictional test invention (then skip step 2). `--profile quick` for a quick run.

## 2. Add the intake

The disclosure goes in **verbatim** through stdin. Do not summarise, tidy or improve it, and add nothing.

```bash
/Users/ahmed/PatentCouncil/tools/council intake --slug <slug> --kind disclosure --stdin <<'EOF'
<the inventor disclosure exactly as given>
EOF
```

Prior art they supply: `--kind prior-art --name <short-name>` (one call per reference). A file already on disk:
`--file <path>` instead of `--stdin`.

## 3. Launch

```bash
/Users/ahmed/PatentCouncil/tools/council run --slug <slug> --background --notify <your session key>
```

It returns at once. Tell the person, in two or three sentences: the matter is running unattended; a Full run is
planned for about two hours; prior-art research and invention capture start in parallel; they will get ten
questions early and updates here as it goes. **Then end your turn.**

## 4. Runner updates

A message starting `[Patent Council update]` is the runner, not the person. **Post its lines to the person
exactly as they are**, as a compact list, and add nothing, with three exceptions:

- **`QUESTIONS`**: read the file it names with the read tool and put the ten questions to the person, numbered,
  each with its options. The run does not wait for them. When they answer, file the answers verbatim
  (`council intake --slug <slug> --kind answers --stdin`), and offer a second pass (section 6).
- **`PAUSED`**: a Claude usage limit. Say the run resumes by itself at the time given; nothing is lost.
- **`FAILED`**: quote the error verbatim. Relaunch once with the section 3 command (it resumes where it stopped:
  finished steps are kept). If it fails again the same way, stop and tell the person what failed.
- **`DELIVERED`**: go to section 5.

If the person asks "any update?", run `council status --slug <slug>` and answer from its `recent`, `done`/`total`
and `elapsed_min` in the same reply.

## 5. When it is delivered

The `DELIVERED` line carries the score, the counts and the four file paths. Read the first lines of
`package/prosecution-assessment.md` for the one sentence behind the score. Then report, in this order: **the
likelihood of grant (N / 10) and that sentence**; the deficiencies by severity and the prior-art references; the
four files (Patent Application and Prosecution Assessment, Word and PDF each) with their full paths. Say once,
plainly: both are drafts for a qualified patent attorney or agent to review at Gate 3, not a filing, and the score
is an AI-assisted estimate, not a legal opinion.

## 6. Second pass with the inventor's answers

After answers are filed, a second pass drafts again from scratch with them (a new run folder; the first is kept):

```bash
/Users/ahmed/PatentCouncil/tools/council run --slug <slug> --run r2 --background --notify <your session key>
```

## Stop, resume, status

- `council stop --slug <slug>`: stops launching new steps; running ones finish. Nothing is deleted.
- `council run --slug <slug> --background --notify <key>`: resumes a stopped, failed or paused run.
- `council status --slug <slug>`: done/total, what is running, any failures, the last dozen ticker lines.

Never delete or recreate a matter to recover from a problem.
