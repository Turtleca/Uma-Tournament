# Uma-Tournament

Welcome to **Uma-Tournament**! This project provides tools and resources for managing tournaments and skills in the context of Umamusume, a Japanese horse girl racing game.

## Project Purpose

This project aims to create a centralized database of trained Umas (Umamusume characters). Using this database, the project ranks each Uma by their performance in specific Champions Meeting conditions, or by their projected performance in Team Trials. It contains programs to compare different Umas on specific tracks, enabling players to analyze, optimize, and select the best performers for various competitive scenarios.

---

## Table of Contents

- [Project Structure](#project-structure)
- [License](#license)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [Credits](#credits)

---

## Project Structure

The repository is organized as follows:

- `uma-skill-tools`  
  *This is a submodule.* It contains tools and utilities related to Umamusume skills, including programs to compare different Umas on specific tracks. For details, see the submodule’s own README or documentation.

- `umamusume-ocr`  
  *This is a submodule.* It provides OCR (Optical Character Recognition) functionality for importing Umamusume trainee-images into a csv.
  
- `umas/`  
  Stores `uma.json` files for use in the tournament.  
  - [`README.md`](https://github.com/Turtleca/Uma-Tournament/blob/main/umas/README.md): Details about the contents and usage of this directory.
  - [`template.json`](https://github.com/Turtleca/Uma-Tournament/blob/main/umas/template.json): A template JSON file for character data.

- `.gitignore`  
  Specifies files and directories to be ignored by Git.

---

## License

This project is licensed under the GNU General Public License v3.0.  
See the [LICENSE](./LICENSE) file for details.

---

## How to Use

1. **Clone the Repository**
   ```bash
   git clone --recurse-submodules https://github.com/Turtleca/Uma-Tournament.git
   ```

2. **Set Up Submodules**
   - The repository uses submodules (`uma-skill-tools`, `umamusume-ocr`).  
     Make sure to initialize and update them:
     ```bash
     git submodule update --init --recursive
     ```

3. **Explore the Code**
   - Review the [`umas/README.md`](https://github.com/Turtleca/Uma-Tournament/blob/main/umas/README.md) for details on the Umamusume json.
   - Check submodule documentation for usage instructions of their respective tools.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes.
4. Submit a pull request with a clear description of your changes.

Please ensure your code is well-documented and tested.

---

## Credits

- [uma-skill-tools](https://github.com/Turtleca/Uma-Tournament/tree/main/uma-skill-tools) and [umamusume-ocr](https://github.com/Turtleca/Uma-Tournament/tree/main/umamusume-ocr) are integrated as submodules—refer to their respective repositories for more information.

---

*For more details, see individual README files within subdirectories and submodules.*
