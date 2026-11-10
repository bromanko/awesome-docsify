> Historical demonstration only. Current project sources; frozen February 2025 catalog. Both proposed changes are held, not ready patches.

# Freshness research

Advisory only; every suggested change requires maintainer review.
No list edits, PRs, comments, or reviews were submitted.

Catalog revision: `35ff2aa3676def959eae5c926c1aaea90aff8a48`
Slice: 0 of 88 (zero-based)
Catalog recheck: unchanged

Sources below are agent-reported observations, not independent verification.

## Entry 55

<pre>class-change.js

The deployed class-change.js site still runs on Docsify. Its HTML loads docsify@4, docsify plugins and the docsify-themeable theme. The listed description closely matches the official GitHub repository description, and the URL is the official homepage. It still fits Showcase.

https://jhildenbiddle.github.io/class-change/
Returns HTTP 200 with no redirect. The HTML loads https://cdn.jsdelivr.net/npm/docsify@4, docsify@4/lib/plugins/search.js, docsify-copy-code@2, docsify-pagination@2, docsify-plugin-ethicalads@1 and docsify-themeable@0 (theme-simple.css).
https://api.github.com/repos/jhildenbiddle/class-change
The canonical repository is jhildenbiddle/class-change and is not archived. Its homepage is https://jhildenbiddle.github.io/class-change. Its description is &#x27;A micro-library for manipulating CSS class names, triggering change events using HTML data attributes, and creating declarative class-related event listeners&#x27;, which matches the catalog wording.
https://raw.githubusercontent.com/jhildenbiddle/class-change/master/README.md
The README links the documentation to https://jhildenbiddle.github.io/class-change and describes the library as an Element.classList alternative for manipulating class names, triggering class change events via data attributes, and declarative class-related listeners. This is consistent with the listing.

Blocking uncertainties:
None reported.

Informational caveats:
The package.json description uses slightly different wording (&#x27;A versatile Element.classList alternative...&#x27;). The catalog wording still matches the repo description, so no change is needed.

Recommendation: keep
Proposed name: None
Proposed URL: None
Proposed description: None</pre>

## Entry 95

<pre>inlets

docs.inlets.dev no longer uses Docsify. The deployed HTML declares a MkDocs / MkDocs Material generator. The official source repository linked from the site, inlets/docs.inlets.dev, is not archived and is still active (last push in Oct 2026). It contains mkdocs.yml with theme &#x27;material&#x27; and no Docsify setup. The listing&#x27;s own description says the docs are &#x27;deployed with docsify&#x27;, and that is now false. A Showcase entry must actually use Docsify, so the official source gives affirmative evidence that it no longer fits.

https://docs.inlets.dev
Returns HTTP 200 at https://docs.inlets.dev/. The HTML has &lt;meta name=&quot;generator&quot; content=&quot;mkdocs-1.5.3, mkdocs-material-9.5.17&quot;&gt; and loads assets/javascripts/bundle.*.min.js (MkDocs Material). No docsify script assets appear.
https://github.com/inlets/docs.inlets.dev
The site links this repository as its source. GitHub API: full_name inlets/docs.inlets.dev, description &#x27;Inlets documentation&#x27;, not archived, pushed_at 2026-10-07. The top-level files are mkdocs.yml, requirements.txt and docs/. There is no Docsify index.html.
https://raw.githubusercontent.com/inlets/docs.inlets.dev/master/mkdocs.yml
The config has site_name: Inlets, site_url: https://docs.inlets.dev/, theme: name: material. This confirms the official build uses MkDocs Material, not Docsify.

Blocking uncertainties:
None reported.

Informational caveats:
I did not check whether another inlets property still uses Docsify. That would be a separate, new listing rather than a correction of this one.
The project itself (inlets) is active. Removal is only about fitting the Docsify Showcase, not about the project&#x27;s health.

Recommendation: remove
Proposed name: None
Proposed URL: None
Proposed description: None</pre>

## Entry 282

<pre>docsify-themeable

docsify-themeable is still a Docsify theme system, and its official site is built with Docsify and the theme itself, so it belongs in Themes. However, the listed &#x27;legacy browser support (IE10+)&#x27; is out of date. The official package.json, the GitHub repository description and the README all say &#x27;legacy browser support (IE11+)&#x27;. Only that browser claim needs correcting. The URL, name and author credit stay as they are.

https://jhildenbiddle.github.io/docsify-themeable
Returns HTTP 200. The HTML loads docsify@4/lib/docsify.min.js and docsify-themeable@0/dist/js/docsify-themeable.min.js along with theme-simple CSS.
https://raw.githubusercontent.com/jhildenbiddle/docsify-themeable/master/package.json
name docsify-themeable, version 0.9.0. Its description is &#x27;A delightfully simple theme system for docsify.js. Features multiple themes with rich customization options, an improved desktop and mobile experience, and legacy browser support (IE11+).&#x27; Keywords include docsify and theme.
https://raw.githubusercontent.com/jhildenbiddle/docsify-themeable/master/README.md
The README says &#x27;legacy browser support (IE11+)&#x27; and lists the feature &#x27;Legacy browser support (IE11+)&#x27;, provided through css-vars-ponyfill.
https://api.github.com/repos/jhildenbiddle/docsify-themeable
The canonical repository is jhildenbiddle/docsify-themeable and is not archived. Its homepage is https://jhildenbiddle.github.io/docsify-themeable. Its description also says IE11+.

Blocking uncertainties:
None reported.

Informational caveats:
I did not test the theme in IE11 or in current browsers.
The deployed site loads docsify@4. I did not check compatibility with any future Docsify major version.

Recommendation: update
Proposed name: None
Proposed URL: None
Proposed description: A delightfully simple theme system for docsify.js. Features multiple themes with rich customization options, an improved desktop and mobile experience, and legacy browser support (IE11+) ([@jhildenbiddle][1]).</pre>


# Proposed pull requests

2 proposed change(s); 0 held for unresolved questions.

### Held
<pre>related: Both queries (&#x27;inlets&#x27; and &#x27;https://docs.inlets.dev&#x27;) returned two closed records. Neither proposes removing the entry or discusses the docs site moving away from Docsify. Issue #119 is alexellis asking about an adopters list. In it, alexellis says docs.inlets.dev uses Docsify (&#x27;I like it mainly because it uses Markdown&#x27;), and a contributor suggests it belongs in Showcase. PR #120, merged 2020-09-03 and approved by jthegedus, added the exact line now in the catalog, including the claim &#x27;is deployed with docsify&#x27;. These records are useful history: they show the entry was added in 2020 because the site used Docsify then. That supports the proposal&#x27;s view that the description was accurate when written and is now stale. There is no open PR proposing the same removal, no maintainer objection to removing it, and no merged PR that already removed it.
{
  &quot;baseline&quot;: {
    &quot;links&quot;: 2,
    &quot;lint&quot;: 1
  },
  &quot;links&quot;: {
    &quot;affected&quot;: [],
    &quot;introduced&quot;: [],
    &quot;passed&quot;: true,
    &quot;preexisting&quot;: [
      &quot;http://corhyam.xyz/&quot;,
      &quot;http://doc.open-uc.cn/&quot;,
      &quot;http://docs.laravel-quickstart.co/&quot;,
      &quot;http://dream0x01.com/spear-framework/&quot;,
      &quot;http://fastdlabs.com/#/&quot;,
      &quot;http://note.taqini.space/&quot;,
      &quot;http://phaser.io/&quot;,
      &quot;http://www.guofei.site/reading/#/&quot;,
      &quot;http://www.zuoziti.com/&quot;,
      &quot;https://abpanic.github.io/Mastering-JavaScript/#/&quot;,
      &quot;https://actions.taio.app/#/&quot;,
      &quot;https://advanced-react-cli.netlify.com/&quot;,
      &quot;https://amzn.github.io/style-dictionary/#/&quot;,
      &quot;https://bitcoinmythbusters.org/&quot;,
      &quot;https://boopathikumar.me/&quot;,
      &quot;https://bradleycwojcik.github.io/euchre-cli/&quot;,
      &quot;https://case.app/&quot;,
      &quot;https://dev.taio.app/#/&quot;,
      &quot;https://docs.case.app/&quot;,
      &quot;https://docs.gitpitch.com/&quot;,
      &quot;https://docs.hathora.dev/&quot;,
      &quot;https://docs.taio.app/#/&quot;,
      &quot;https://docsify-darklight-theme.boopathikumar.me/&quot;,
      &quot;https://fairlay.com/api/#/&quot;,
      &quot;https://fastdocs.io/&quot;,
      &quot;https://fmartinou.github.io/whats-up-docker/&quot;,
      &quot;https://github.com/Brannua/docsify-pagination-keyboard-helper&quot;,
      &quot;https://github.com/mitchell-b-chelin/WPDocsify&quot;,
      &quot;https://github.com/pikapikapikaori/docsify-gitalk-with-footer&quot;,
      &quot;https://greybax.github.com/awesome-IT-films&quot;,
      &quot;https://hmpljs.github.io/&quot;,
      &quot;https://livere.com/&quot;,
      &quot;https://mouday.github.io/coding-tree/&quot;,
      &quot;https://posthtml.org/&quot;,
      &quot;https://pyecharts.org/&quot;,
      &quot;https://runkit.com/home&quot;,
      &quot;https://skuber.co/&quot;,
      &quot;https://super-detype.superkenil.com/#/&quot;,
      &quot;https://thirdwavecoffeebase.com/#/&quot;,
      &quot;https://veal98.gitee.io/cs-wiki/#/&quot;,
      &quot;https://wiki.airqo.net/&quot;,
      &quot;https://www.ethicalads.io/&quot;,
      &quot;https://www.explorewanchain.org/&quot;,
      &quot;https://yangchunjian.com/&quot;,
      &quot;https://yjava.cn/&quot;
    ],
    &quot;unverified&quot;: []
  },
  &quot;passed&quot;: false,
  &quot;patched&quot;: {
    &quot;links&quot;: 2,
    &quot;lint&quot;: 1
  },
  &quot;reason&quot;: &quot;Proposed edit failed checks; held for maintainer review. See validation logs.&quot;
}</pre>
<pre>Searches:
repo:docsifyjs/awesome-docsify &quot;inlets&quot; in:title,body,comments
repo:docsifyjs/awesome-docsify &quot;https://docs.inlets.dev&quot; in:title,body,comments
References:
https://github.com/docsifyjs/awesome-docsify/pull/120
https://github.com/docsifyjs/awesome-docsify/issues/119
https://github.com/docsifyjs/awesome-docsify/issues/119#issuecomment-683392773
https://github.com/docsifyjs/awesome-docsify/issues/119#issuecomment-683392726</pre>

## entry-95

<pre>Remove inlets entry

docs.inlets.dev no longer uses Docsify. The deployed HTML declares a MkDocs / MkDocs Material generator. The official source repository linked from the site, inlets/docs.inlets.dev, is not archived and is still active (last push in Oct 2026). It contains mkdocs.yml with theme &#x27;material&#x27; and no Docsify setup. The listing&#x27;s own description says the docs are &#x27;deployed with docsify&#x27;, and that is now false. A Showcase entry must actually use Docsify, so the official source gives affirmative evidence that it no longer fits.

Evidence:
https://docs.inlets.dev — Returns HTTP 200 at https://docs.inlets.dev/. The HTML has &lt;meta name=&quot;generator&quot; content=&quot;mkdocs-1.5.3, mkdocs-material-9.5.17&quot;&gt; and loads assets/javascripts/bundle.*.min.js (MkDocs Material). No docsify script assets appear.
https://github.com/inlets/docs.inlets.dev — The site links this repository as its source. GitHub API: full_name inlets/docs.inlets.dev, description &#x27;Inlets documentation&#x27;, not archived, pushed_at 2026-10-07. The top-level files are mkdocs.yml, requirements.txt and docs/. There is no Docsify index.html.
https://raw.githubusercontent.com/inlets/docs.inlets.dev/master/mkdocs.yml — The config has site_name: Inlets, site_url: https://docs.inlets.dev/, theme: name: material. This confirms the official build uses MkDocs Material, not Docsify.

Informational caveats:
I did not check whether another inlets property still uses Docsify. That would be a separate, new listing rather than a correction of this one.
The project itself (inlets) is active. Removal is only about fitting the Docsify Showcase, not about the project&#x27;s health.

Based on catalog revision 35ff2aa3676def959eae5c926c1aaea90aff8a48.
Proposed by an automated freshness review. A maintainer must verify the evidence and edit.
Validation and discussion checks are recorded below.

Review status: Held
Prior discussion: related: Both queries (&#x27;inlets&#x27; and &#x27;https://docs.inlets.dev&#x27;) returned two closed records. Neither proposes removing the entry or discusses the docs site moving away from Docsify. Issue #119 is alexellis asking about an adopters list. In it, alexellis says docs.inlets.dev uses Docsify (&#x27;I like it mainly because it uses Markdown&#x27;), and a contributor suggests it belongs in Showcase. PR #120, merged 2020-09-03 and approved by jthegedus, added the exact line now in the catalog, including the claim &#x27;is deployed with docsify&#x27;. These records are useful history: they show the entry was added in 2020 because the site used Docsify then. That supports the proposal&#x27;s view that the description was accurate when written and is now stale. There is no open PR proposing the same removal, no maintainer objection to removing it, and no merged PR that already removed it.
Validation: Proposed edit failed checks; held for maintainer review. See validation logs.
</pre>

```diff
--- a/README.md
+++ b/README.md
@@ -92,7 +92,6 @@
 - [euchre-cli](https://bradleycwojcik.github.io/euchre-cli/) - Play euchre in your terminal.
 - [fastdocs.io](https://fastdocs.io/) - Instantly deploy your docs with Docsify without any code!
 - [Anki](https://docs.ankiweb.net/) - A powerful cross-platform flashcard program which makes remembering things easy.
-- [inlets](https://docs.inlets.dev) - The documentation for inlets ("The Cloud Native Tunnel") is deployed with docsify.
 - [Cypher Notepad](https://cypher-notepad.github.io/wiki/#/?coverpage=false) - The user-friendly, plain-text editor with Hybrid Encryption.
 - [advanced-react-cli](https://advanced-react-cli.netlify.com/) - NPM package which aims to provide a better way to install packages for your react application through an intuitive CLI.
 - [GitPitch.com](https://docs.gitpitch.com/) - The perfect slide deck solution for Tech Conferences, Training, Developer Advocates, and Educators.
```

### Held
<pre>related: The search used &#x27;docsify-themeable&#x27; and its homepage URL and returned three merged PRs. None of them makes or rejects the IE10+ to IE11+ correction. PR #7, by the author jhildenbiddle and merged 2018-06-07, added the entry with &#x27;full legacy support (IE10+)&#x27;. PR #9, also by the author and merged 2018-06-12, changed that wording to &#x27;legacy browser support (IE10+)&#x27; and kept IE10+. That was accurate for upstream at the time. These records explain where the current text came from, but neither one changed the browser version. PR #93 (Restish showcase) only mentions docsify-themeable as a styling dependency and has nothing to do with this entry. There is no open competing PR, no maintainer rejection, and no merged PR that already changed the text to IE11+.
{
  &quot;baseline&quot;: {
    &quot;links&quot;: 2,
    &quot;lint&quot;: 1
  },
  &quot;links&quot;: {
    &quot;affected&quot;: [],
    &quot;introduced&quot;: [],
    &quot;passed&quot;: true,
    &quot;preexisting&quot;: [
      &quot;http://corhyam.xyz/&quot;,
      &quot;http://doc.open-uc.cn/&quot;,
      &quot;http://docs.laravel-quickstart.co/&quot;,
      &quot;http://dream0x01.com/spear-framework/&quot;,
      &quot;http://fastdlabs.com/#/&quot;,
      &quot;http://note.taqini.space/&quot;,
      &quot;http://phaser.io/&quot;,
      &quot;http://www.guofei.site/reading/#/&quot;,
      &quot;http://www.zuoziti.com/&quot;,
      &quot;https://abpanic.github.io/Mastering-JavaScript/#/&quot;,
      &quot;https://actions.taio.app/#/&quot;,
      &quot;https://advanced-react-cli.netlify.com/&quot;,
      &quot;https://amzn.github.io/style-dictionary/#/&quot;,
      &quot;https://bitcoinmythbusters.org/&quot;,
      &quot;https://boopathikumar.me/&quot;,
      &quot;https://bradleycwojcik.github.io/euchre-cli/&quot;,
      &quot;https://case.app/&quot;,
      &quot;https://dev.taio.app/#/&quot;,
      &quot;https://docs.case.app/&quot;,
      &quot;https://docs.gitpitch.com/&quot;,
      &quot;https://docs.hathora.dev/&quot;,
      &quot;https://docs.taio.app/#/&quot;,
      &quot;https://docsify-darklight-theme.boopathikumar.me/&quot;,
      &quot;https://fairlay.com/api/#/&quot;,
      &quot;https://fastdocs.io/&quot;,
      &quot;https://fmartinou.github.io/whats-up-docker/&quot;,
      &quot;https://gallery.pyecharts.org/&quot;,
      &quot;https://github.com/Brannua/docsify-pagination-keyboard-helper&quot;,
      &quot;https://github.com/mitchell-b-chelin/WPDocsify&quot;,
      &quot;https://github.com/pikapikapikaori/docsify-gitalk-with-footer&quot;,
      &quot;https://greybax.github.com/awesome-IT-films&quot;,
      &quot;https://hmpljs.github.io/&quot;,
      &quot;https://livere.com/&quot;,
      &quot;https://mouday.github.io/coding-tree/&quot;,
      &quot;https://posthtml.org/&quot;,
      &quot;https://pyecharts.org/&quot;,
      &quot;https://runkit.com/home&quot;,
      &quot;https://skuber.co/&quot;,
      &quot;https://super-detype.superkenil.com/#/&quot;,
      &quot;https://thirdwavecoffeebase.com/#/&quot;,
      &quot;https://veal98.gitee.io/cs-wiki/#/&quot;,
      &quot;https://wiki.airqo.net/&quot;,
      &quot;https://www.ethicalads.io/&quot;,
      &quot;https://www.explorewanchain.org/&quot;,
      &quot;https://yangchunjian.com/&quot;,
      &quot;https://yjava.cn/&quot;
    ],
    &quot;unverified&quot;: []
  },
  &quot;passed&quot;: false,
  &quot;patched&quot;: {
    &quot;links&quot;: 2,
    &quot;lint&quot;: 1
  },
  &quot;reason&quot;: &quot;Proposed edit failed checks; held for maintainer review. See validation logs.&quot;
}</pre>
<pre>Searches:
repo:docsifyjs/awesome-docsify &quot;docsify-themeable&quot; in:title,body,comments
repo:docsifyjs/awesome-docsify &quot;https://jhildenbiddle.github.io/docsify-themeable&quot; in:title,body,comments
References:
https://github.com/docsifyjs/awesome-docsify/pull/7
https://github.com/docsifyjs/awesome-docsify/pull/9</pre>

## entry-282

<pre>Update docsify-themeable entry

docsify-themeable is still a Docsify theme system, and its official site is built with Docsify and the theme itself, so it belongs in Themes. However, the listed &#x27;legacy browser support (IE10+)&#x27; is out of date. The official package.json, the GitHub repository description and the README all say &#x27;legacy browser support (IE11+)&#x27;. Only that browser claim needs correcting. The URL, name and author credit stay as they are.

Evidence:
https://jhildenbiddle.github.io/docsify-themeable — Returns HTTP 200. The HTML loads docsify@4/lib/docsify.min.js and docsify-themeable@0/dist/js/docsify-themeable.min.js along with theme-simple CSS.
https://raw.githubusercontent.com/jhildenbiddle/docsify-themeable/master/package.json — name docsify-themeable, version 0.9.0. Its description is &#x27;A delightfully simple theme system for docsify.js. Features multiple themes with rich customization options, an improved desktop and mobile experience, and legacy browser support (IE11+).&#x27; Keywords include docsify and theme.
https://raw.githubusercontent.com/jhildenbiddle/docsify-themeable/master/README.md — The README says &#x27;legacy browser support (IE11+)&#x27; and lists the feature &#x27;Legacy browser support (IE11+)&#x27;, provided through css-vars-ponyfill.
https://api.github.com/repos/jhildenbiddle/docsify-themeable — The canonical repository is jhildenbiddle/docsify-themeable and is not archived. Its homepage is https://jhildenbiddle.github.io/docsify-themeable. Its description also says IE11+.

Informational caveats:
I did not test the theme in IE11 or in current browsers.
The deployed site loads docsify@4. I did not check compatibility with any future Docsify major version.

Based on catalog revision 35ff2aa3676def959eae5c926c1aaea90aff8a48.
Proposed by an automated freshness review. A maintainer must verify the evidence and edit.
Validation and discussion checks are recorded below.

Review status: Held
Prior discussion: related: The search used &#x27;docsify-themeable&#x27; and its homepage URL and returned three merged PRs. None of them makes or rejects the IE10+ to IE11+ correction. PR #7, by the author jhildenbiddle and merged 2018-06-07, added the entry with &#x27;full legacy support (IE10+)&#x27;. PR #9, also by the author and merged 2018-06-12, changed that wording to &#x27;legacy browser support (IE10+)&#x27; and kept IE10+. That was accurate for upstream at the time. These records explain where the current text came from, but neither one changed the browser version. PR #93 (Restish showcase) only mentions docsify-themeable as a styling dependency and has nothing to do with this entry. There is no open competing PR, no maintainer rejection, and no merged PR that already changed the text to IE11+.
Validation: Proposed edit failed checks; held for maintainer review. See validation logs.
</pre>

```diff
--- a/README.md
+++ b/README.md
@@ -279,7 +279,7 @@
 
 ## Themes
 
-- [docsify-themeable](https://jhildenbiddle.github.io/docsify-themeable) - A delightfully simple theme system for docsify.js. Features multiple themes with rich customization options, an improved desktop and mobile experience, and legacy browser support (IE10+) ([@jhildenbiddle][1]).
+- [docsify-themeable](https://jhildenbiddle.github.io/docsify-themeable) - A delightfully simple theme system for docsify.js. Features multiple themes with rich customization options, an improved desktop and mobile experience, and legacy browser support (IE11+) ([@jhildenbiddle][1]).
 - [🌙 docsify-darkly-theme](https://github.com/sushantrahate/docsify-darkly-theme) - Dark theme for docsify. [@sushantrahate](https://github.com/sushantrahate).
 - [:first_quarter_moon:docsify-darklight-theme](https://github.com/boopathikumar018/docsify-darklight-theme) - It is a simple and highly customizable theme for docsify.js. Using this theme, documents will have a theme switcher to switch between `dark-mode` and `light-mode`. See [preview](https://docsify-darklight-theme.boopathikumar.me) here. [@boopathikumar](https://boopathikumar.me/).
 - [🧛🏻docsify-theme-darcula](https://github.com/A5yncX/docsify-theme-darcula) - A comfortable darcula style dark theme. [Preview](https://mellow-crepe-abaf27.netlify.app/docs/#/) . ([@A5yncX](https://github.com/A5yncX))
```
