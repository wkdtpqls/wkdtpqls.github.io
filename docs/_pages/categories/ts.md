---
layout: archive
permalink: typescript
title: "타입스크립트"
author_profile: true
sidebar:
  nav: "sidebar-categroy"
---

{% assign posts = site.categories.typescript %}
{% for post in posts %}
  {% include custom-archive-single.html type=entries_layout %}
{% endfor %}