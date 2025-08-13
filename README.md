![CI](https://github.com/dhoepp/devTips/actions/workflows/python-app.yml/badge.svg)

# DevTips

A simple Python script that displays random development tips to help improve your coding workflow and practices.

## Features

- **Random Selection**: Each time you run the script, a different tip is randomly selected from our collection
- **23 Curated Tips**: Covers various aspects of development including Git, code quality, debugging, and best practices
- **Simple CLI**: Easy to run from command line or integrate into your development workflow

## Usage

```bash
python dev_tip.py
```

## Tips Collection

The script includes tips on:
- Git workflow and version control
- Code quality and best practices
- Debugging and troubleshooting
- Development environment setup
- Testing and automation
- Documentation and naming conventions

## Randomization Approach

The application uses Python's built-in `random.choice()` function to select tips. This ensures:
- **True randomness**: Each tip has an equal probability of being selected
- **No repetition prevention**: You might see the same tip multiple times, which is intentional for reinforcement
- **Simplicity**: No complex state management or tracking required
- **Instant results**: No delays or setup needed

## Development

### Running Tests

```bash
python test_dev_tip.py
```

### Linting

```bash
flake8 dev_tip.py test_dev_tip.py
```

### Adding New Tips

To add new tips, simply append them to the `tips` list in `dev_tip.py`. Each tip should be:
- A single string
- Clear and actionable
- Relevant to software development
- Concise (ideally one sentence)
