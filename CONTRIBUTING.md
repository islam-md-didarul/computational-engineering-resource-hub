# Contributing

Thank you for helping improve the Computational Engineering Resource Hub.

## Suggesting a resource

Use the **Resource suggestion** issue template or submit a pull request that updates `data/resources.json`.

A strong addition should:

- directly support computational engineering learning or practice;
- come from an authoritative, educational, or well-maintained source;
- have a stable public URL;
- avoid pirated books, unauthorized copies, and unsafe downloads;
- include an original, concise description;
- use an existing category where possible;
- declare whether the resource is fully free or has mixed/paid access.

## Pull request workflow

1. Fork the repository.
2. Create a branch such as `add-petsc-course`.
3. Edit `data/resources.json`.
4. Validate the data and regenerate the README:

   ```bash
   python scripts/validate_resources.py
   python scripts/generate_readme.py
   ```

5. Review the rendered `README.md` on GitHub or in a Markdown preview.
6. Open a pull request and explain why the resource is useful.

## Style

- Use sentence case for titles and descriptions.
- Keep descriptions below 180 characters when practical.
- Use lowercase kebab-case tags.
- Avoid promotional claims such as “best,” “ultimate,” or “must use.”
- Prefer official documentation and primary educational sources.
