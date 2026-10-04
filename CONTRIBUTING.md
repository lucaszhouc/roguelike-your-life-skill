# Contributing

## Before opening a pull request

- Keep examples fictional or anonymized.
- Do not add real names, personal handles, private project details, credentials, local machine paths, or private conversation excerpts.
- Keep the distinction between facts, inference, and uncertainty explicit in prompts and schemas.
- Explain the behavioral reason for a change and include a small reproducible example when possible.

## Validation

Run the following checks from the repository root:

```text
python -m json.tool skill.json
python -m py_compile tools/stitch_scroll.py
python tools/stitch_scroll.py --help
```

If you change the image stitching tool, also run it against a fictional sample image and verify the output dimensions and file format.

## Maintenance model

This is a small, single-maintainer project. Pull requests may take time to receive a response. For security reports or time-sensitive questions, email `lucaszhouc@gmail.com`. If you need a different maintenance cadence, you are welcome to fork the repository.

AI-assisted contributions are welcome when the contributor can explain the changed behavior and has checked the resulting files.
