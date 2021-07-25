# CSS

- [CSS](#css)
  - [Specificity](#specificity)
  - [CSS Selectors](#css-selectors)
  - [Responsive Design](#responsive-design)
  - [SCSS](#scss)
    - [Compile SCSS:](#compile-scss)
    - [Auto Compile SCSS:](#auto-compile-scss)

## Specificity

1. Inline
2. Id
3. Class
4. Type

## CSS Selectors

|Code|Description|
|-|-|
|a, b|Multiple Element Selector|
|a b|Descendent Selector|
|a > b|Child Selector|
|a + b|Adjacent Sibling Selector|
|[a=b]|Attribute Selector|
|a:b|PseudoClass Selector|
|a::b|PseudoElement Selector|

## Responsive Design

|Type|Example|
|-|-|
|Viewport|`<meta name="viewport" content="width=device-width, initial-scale=1.0">`|
|Media Queries|**Media Types**: print, screen, ... <br/> **Media Features**: height, width, orientation, ...|
|Flexbox||
|Grids||

## SCSS

### Compile SCSS:

sass `<name>`.scss:`<name>`.css

### Auto Compile SCSS:

sass --watch `<name>`.scss:`<name>`.css
