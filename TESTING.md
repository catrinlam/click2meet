# Testing

This is the TESTING file for the [click2meet](https://click2meet-4e32aa494605.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

## Testing Contents  
  
- [Testing](#testing)
  - [Testing Contents](#testing-contents)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Evaluation](#wave-accessibility-evaluation)
  - [Unit Testing](#unit-testing)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Testing User Stories](#testing-user-stories)
  - [Bugs](#bugs)


## Validation

### HTML Validation

[HTML validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fstitchin-aa280977732a.herokuapp.com%2F)

![HTML validation](docs/testing/html_valid.png)

| HTML Source Code/Page | Errors | Warnings | Note                             |
| --------------------- | ------ | -------- | -------------------------------- |
| Home                  | 0      | 0        |                                  |
| Sign In               | 0      | 0        |                                  |
| [Sign Up](docs/testing/html_signup.png)               | 1      | 0        | Error based on built-in Django form       |
| Pattern Detail        | 0      | 0        |                                  |
| Post Pattern          | 0      | 0        |                                  |
| Delete Comment        | 0      | 0        | |
| View Favourites       | 0      | 0        |                                  |
| Log Out               | 0      | 0        |                                  |
| Forgot Password       | 0      | 0        | 

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the small amount of JavaScript code added to the project.

| File          | Screenshot | Notes |
|---------------|------------|-------|
| scripts.js | ![JS validation on sctipts](docs/testing/js.png) | No errors found |

**Note:** The `/*jshint esversion: 6 */` directive was added to the top of the JavaScript files to specify the ECMAScript version.

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files.

| File       | Screenshot | Notes |
|------------|------------|-------|
| admin.py   | ![Validation on admin.py](docs/testing/py_admin.png) | No errors found |
| forms.py   | ![Validation on forms.py](docs/testing/py_forms.png) | No errors found |
| models.py  | ![Validation on models.py](docs/testing/py_models.png) | No errors found |
| urls.py    | ![Validation on urls.py](docs/testing/py_urls.png) | No errors found |
| views.py   | ![Validation on views.py](docs/testing/py_views.png) | No errors found |

### CSS Validation 

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS file.

![CSS validation](docs/testing/css_valid.png)
  
<hr> 
   
### Lighthouse Scores

Lighthouse testing was carried out in Incognito mode to achieve the best result.

**Desktop**  

![Lighthouse scores desktop](docs/testing/desktop_lh.png)  
*Desktop Home Page*  
  
![Lighthouse scores desktop](docs/testing/dt_pattern_lh.png)  
*Desktop Event Details Page*

**Mobile**  

![Lighthouse scores mobile](docs/testing/mobile_lh.png) 
*Mobile Home Page*  
  
![Lighthouse scores mobile](docs/testing/mob_pattern_lh.png) 
*Mobile Event Details Page*
  
<hr>  

### Wave Accessibility Evaluation

[Wave Accessibility Evaluation](https://wave.webaim.org/) was used to check the accessibility of the page.

<img src="docs/testing/access_report.png" alt="Wave Accessibility Evaluation" height="500px">  

<hr>  

## Manual Testing

### Testing User Stories

User Stories are documented in the [Stitchin GitHub Projects Board](https://github.com/users/catrinlam/projects/6).

| User Story                                                                                               | Met Acceptance Criteria                                                                 | Response                                                                                 | Pass/Fail | Fix |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------|-----|

<hr>
  
## Bugs  
  

