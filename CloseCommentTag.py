#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sublime
import sublime_plugin
import re


regexAll = re.compile('<([a-zA-Z0-9/ _=;\"\.\-]+)>')
regexTagname = re.compile('(^[a-zA-Z0-9]+)')
regexNonCloseTag = re.compile(
    '^(br|wbr|hr|img|col|base|link|meta|input|keygen|area|param|embed|source|track|command)')
regexIdname = re.compile('id="([\w\-]+)"')
regexClassname = re.compile('class="([\w\- _]+)')


class CloseCommentTagVars():
    pass


class InsertCommentTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # 文書の初めから現在のキャレット位置までのタグを取得
        regionLeftOfCursor = self.view.substr(sublime.Region(0, self.view.sel()[0].begin()))
        tags = regexAll.findall(regionLeftOfCursor)
        openTags = []
        currentOpenTag = ''
        closeCommentTagVars = CloseCommentTagVars()
        closeTag = '<!-- /%s%s -->'

        # タグの一覧から閉じられていないタグの取得
        for tag in tags:
            if not regexNonCloseTag.findall(tag):
                if tag[0] == '/':
                    currentCloseTag = tag[1:]
                    openTagsLast = "".join(regexTagname.findall(openTags[-1]))

                    if currentCloseTag == openTagsLast:
                        openTags.pop()
                else:
                    openTags.append(tag)

        # 閉じられていないタグ一覧から閉じタグが必要な直近の要素を取得
        openTags.reverse()

        for openTag in openTags:
            if not regexNonCloseTag.findall(openTag):
                currentOpenTag = openTag
                break

        # id, class名の取得
        closeCommentTagVars.tagname = "".join(regexTagname.findall(currentOpenTag))
        closeCommentTagVars.id = "".join(regexIdname.findall(currentOpenTag))
        closeCommentTagVars.classname = "".join(regexClassname.findall(currentOpenTag))
        closeCommentTagVars.classname = closeCommentTagVars.classname.replace(' ', '.')

        # キャレットの前にid, class名付きのコメントを挿入
        if closeCommentTagVars.id:
            closeCommentTagVars.id = '#' + closeCommentTagVars.id

        if closeCommentTagVars.classname:
            closeCommentTagVars.classname = '.' + closeCommentTagVars.classname

        self.view.insert(
            edit,
            self.view.sel()[0].begin(),
            closeTag % (closeCommentTagVars.id, closeCommentTagVars.classname))
