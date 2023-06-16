+++
title = "Git Submission Information Specification"
description = "Git Submission Information Specification"
date = 2023-06-16
draft = false

[taxonomies]
categories = ["Safari"]
tags = ["Norm"]
[extra]
keywords = "Git, Norm"
+++

This is the function lists of travel website design.

<!-- more -->

```git
<类型>[可选 范围]: <描述>

[可选 正文]

[可选 脚注]
```

类型：

- fix: 修复类型用于标识与向后兼容错误修复相关的生产更改。
- feat: 用于标识与新的向后兼容能力或功能相关的生产更改。
- BREAKING CHANGE 在范围之后添加的 `!` 提醒注意破坏性提交 (脚注)
- build/chore: 识别与构建系统（涉及脚本、配置或工具）和软件包依赖关系相关的开发变更。
- ci: ci 类型用于标识与持续集成和部署系统相关的开发更改 - 涉及脚本、配置或工具。
- docs: docs 类型用于标识与项目相关的文档更改 - 无论是外部的最终用户（在库的情况下）还是内部的开发人员。
- style: 样式类型用于标识与样式化代码库相关的开发更改，而不管其含义如何 - 例如缩进、分号、引号、尾随逗号等。
- refactor: 重构类型用于标识与修改代码库相关的开发更改，其既不添加功能也不修复错误 - 例如删除冗余代码，简化代码，重命名变量等。
- perf: perf 类型用于标识与向后兼容性能改进相关的生产更改。
- test: 测试类型用于标识与测试相关的开发更改 - 例如重构现有测试或添加新测试。

## 约定式提交规范

> 本文中的关键词“必须（MUST）”、“禁止（MUST NOT）”、“必要（REQUIRED）”、“应当（SHALL）”、“不应当（SHALL NOT）”、“应该（SHOULD）”、“不应该（SHOULD NOT）”、“推荐（RECOMMENDED）”、“可以（MAY）”和“可选（OPTIONAL）” ，其相关解释参考 RFC 2119。
> 每个提交都必须使用类型字段前缀，它由一个名词构成，诸如 feat 或 fix，其后接可选的范围字段，可选的 !，以及必要的冒号（英文半角）和空格。
当一个提交为应用或类库实现了新功能时，必须使用 feat 类型。
当一个提交为应用修复了 bug 时，必须使用 fix 类型。
范围字段可以跟随在类型字段后面。范围必须是一个描述某部分代码的名词，并用圆括号包围，例如：fix(parser):
描述字段必须直接跟在 <类型>(范围) 前缀的冒号和空格之后。描述指的是对代码变更的简短总结，例如：fix: array parsing issue when multiple spaces were contained in string。
在简短描述之后，可以编写较长的提交正文，为代码变更提供额外的上下文信息。正文必须起始于描述字段结束的一个空行后。
提交的正文内容自由编写，并可以使用空行分隔不同段落。
在正文结束的一个空行之后，可以编写一行或多行脚注。每行脚注都必须包含 一个令牌（token），后面紧跟 `:<space>` 或 `<space>`# 作为分隔符，后面再紧跟令牌的值（受 git trailer convention 启发）。
脚注的令牌必须使用 - 作为连字符，比如 Acked-by (这样有助于 区分脚注和多行正文)。有一种例外情况就是 sBREAKING CHANGE，它可以被认为是一个令牌。
脚注的值可以包含空格和换行，值的解析过程必须直到下一个脚注的令牌/分隔符出现为止。
破坏性变更必须在提交信息中标记出来，要么在 <类型>(范围) 前缀中标记，要么作为脚注的一项。
包含在脚注中时，破坏性变更必须包含大写的文本 BREAKING CHANGE，后面紧跟着冒号、空格，然后是描述，例如：BREAKING CHANGE: environment variables now take precedence over config files。
包含在 <类型>(范围) 前缀时，破坏性变更必须通过把 ! 直接放在 : 前面标记出来。如果使用了 !，那么脚注中可以不写 BREAKING CHANGE:，同时提交信息的描述中应该用来描述破坏性变更。
在提交说明中，可以使用 feat 和 fix 之外的类型，比如：docs: updated ref docs. 。
工具的实现必须不区分大小写地解析构成约定式提交的信息单元，只有 BREAKING CHANGE 必须是大写的。
BREAKING-CHANGE 作为脚注的令牌时必须是 BREAKING CHANGE 的同义词。

## Reference

- [约定式提交](https://www.conventionalcommits.org/zh-hans/v1.0.0/)
- [Angular 提交信息规范](https://zj-git-guide.readthedocs.io/zh_CN/latest/message/Angular%E6%8F%90%E4%BA%A4%E4%BF%A1%E6%81%AF%E8%A7%84%E8%8C%83/)
- [Understanding Semantic Commit Messages Using Git and Angular](https://nitayneeman.com/posts/understanding-semantic-commit-messages-using-git-and-angular/)
- [Git 约定式提交规范实践](https://www.barretlee.com/blog/2019/10/28/commit-convention/)
