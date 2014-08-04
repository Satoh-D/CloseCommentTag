CloseCommentTag
===============

_Insert comment tag like a "&lt;!-- /#id.classname --&gt;" before closing tag._  
HTMLの閉じタグの前にコメントを入れるプラグイン

## Usage

Before. 

```html
<div id="hoge" class="fuga">
Hoge
</div>

<p id="foo" class="bar test">
Hoge
</p>
```

After
```html
<div id="hoge" class="fuga">
Hoge
<!-- /#hoge.fuga --></div>

<p id="foo" class="bar test">
Hoge
<!-- /#foo.bar.test --></p>
```

1. Move the caret "&lt;/div&gt;" on top of the "&lt;".
2. Push <kbd>shift</kbd>+<kbd>command</kbd>+<kbd>,</kbd> or Select "Package Control" -> "CloseCommentTag: Insert comment tag."
3. Before the closing tag put the "&lt;!-- /#hoge.fuga --&gt;"

## Keymap

- Windows: <kbd>shift</kbd>+<kbd>ctrl</kbd>+<kbd>,</kbd>
- OSX: <kbd>shift</kbd>+<kbd>command</kbd>+<kbd>,</kbd>
- Linux: <kbd>shift</kbd>+<kbd>command</kbd>+<kbd>,</kbd>

## Install

1. select "Package Control: Add Repository"
2. input "https://github.com/Satoh-D/CloseCommentTag"
3. select "Package Control: Install Package"
4. input "CloseCommentTag"

## Licence

[MIT License](https://github.com/tcnksm/tool/blob/master/LICENCE) 

## Author

[Sato Daiki(@Satoh_D)](https://twitter.com/Satoh_D)
