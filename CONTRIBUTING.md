# Contributing to Call Center Workforce Planning Toolkit

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🎯 Areas for Contribution

### Documentation
- Improve existing guides with clearer explanations
- Add real-world case studies and examples
- Translate documentation to other languages
- Create video tutorials or interactive demos

### Data & Examples
- Contribute anonymized real call center datasets
- Add industry-specific examples (retail, healthcare, finance, tech support)
- Create edge case scenarios for testing
- Add seasonal pattern variations

### Formulas & Tools
- Implement Erlang X (abandonment) formulas
- Create multi-skill routing calculators
- Build real-time adherence tracking tools
- Develop shift schedule optimization algorithms
- Add Python/R statistical analysis scripts

### Validation & Testing
- Validate formulas against real-world data
- Compare model predictions to actual outcomes
- Test edge cases and boundary conditions
- Performance benchmarking

## 📝 How to Contribute

### For Documentation Improvements
1. Fork the repository
2. Create a branch: `git checkout -b docs/improve-erlang-guide`
3. Make your changes
4. Submit a pull request with a clear description

### For New Features
1. Open an issue first to discuss the feature
2. Fork and create a feature branch
3. Implement with clear comments
4. Add documentation and examples
5. Submit a pull request

### For Bug Fixes
1. Open an issue describing the bug
2. Fork and create a bugfix branch
3. Fix the issue with test cases
4. Submit a pull request referencing the issue

## 📋 Pull Request Guidelines

### Good PR Checklist
- [ ] Clear, descriptive title
- [ ] Detailed description of changes
- [ ] Documentation updated if needed
- [ ] Examples provided for new features
- [ ] Formulas validated against known results
- [ ] No breaking changes to existing files (unless discussed)

### PR Description Template
```markdown
## What does this PR do?
Brief description of changes

## Why is this needed?
Explain the problem this solves

## How was it tested?
Describe validation/testing performed

## Screenshots/Examples
If applicable, add examples of output
```

## 🔬 Testing Guidelines

### For Formula Changes
- Validate against published Erlang C tables
- Test with edge cases (very low/high traffic)
- Ensure Excel formulas work in Excel 2016+
- Check for #DIV/0!, #NUM!, #REF! errors

### For Data Changes
- Ensure CSV format consistency
- Validate data ranges are realistic
- Check for missing values
- Verify column headers match documentation

## 📐 Code Style

### Excel Formulas
- Use descriptive column names
- Include formula comments in adjacent cells
- Break complex formulas into intermediate steps
- Provide both simplified and exact versions

### Python Scripts
- Follow PEP 8 style guide
- Include docstrings for functions
- Add type hints where helpful
- Keep scripts dependency-light

### Markdown Documentation
- Use clear headings hierarchy
- Include code examples with syntax highlighting
- Add tables for comparative data
- Use emojis sparingly for visual navigation

## 🌟 Recognition

Contributors will be acknowledged in:
- README.md Contributors section
- Release notes for significant contributions
- Documentation headers for major additions

## ❓ Questions?

- Open a GitHub Discussion for general questions
- Create an Issue for bugs or feature requests
- Tag with appropriate labels (documentation, enhancement, bug, etc.)

## 📜 Code of Conduct

### Our Standards
- Be respectful and inclusive
- Welcome newcomers and learners
- Focus on constructive feedback
- Respect different experience levels

### Not Acceptable
- Harassment or discriminatory language
- Personal attacks or trolling
- Sharing private information
- Unethical or illegal content

## 🎓 Learning Contributions

Even if you're new to workforce planning:
- Ask clarifying questions in Issues
- Suggest documentation improvements
- Share your learning journey
- Report confusing sections

All contributions, big or small, are valued!

## 📞 Contact

For sensitive issues or private discussions:
- Open a private discussion on GitHub
- Tag maintainers directly

---

Thank you for helping improve workforce planning for call centers worldwide! 🙏
