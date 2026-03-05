<a href="https://software.sil.org/wp/wp-content/uploads/2019/03/MingzatTitle.png"><img class="alignnone size-full wp-image-3171" src="https://software.sil.org/wp/wp-content/uploads/2019/03/MingzatTitle.png" alt="" width="276" height="161" /></a>

<h2>Mingzat — A beautiful Lepcha font</h2>

Mingzat is a font for the Lepcha script which is used by the <a href="https://www.ethnologue.com/language/lep" title="" class="external">Lepcha language</a> of South Asia. The name "Mingzat" means <em>"treasure of letters"</em> in the Lepcha language.

<strong>Mingzat</strong> is a Unicode font based on Jason Glavy's <strong>JG Lepcha</strong> custom-encoded font. With his generous permission we have used his design and released the font under the <a href="https://openfontlicense.org/" title="" class="external">SIL Open Font License (OFL)</a>.

<h3>Supported character ranges</h3>

<table>
<thead>
<tr>
  <th>Unicode block</th>
  <th>Mingzat support</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Lepcha (complete)</td>
  <td>U+1C00..U+1C4F</td>
</tr>
<tr>
  <td>Codepage 1252 (Western)¹</td>
  <td>✓</td>
</tr>
</tbody>
</table>

¹Inclusion of basic Latin repertoire is provided as a convenience, e.g., for use in menus or for displaying markup in text files. These fonts are not intended for extensive Latin script use.

This <a href="https://software.sil.org/downloads/r/mingzat/Mingzat-typesample.pdf">Type Sample</a> document demonstrates the characters and a sample text.

<h3>Rendering Issues</h3>

Lepcha is a complex Indic script which requires reordering. The font has been tested to work on Microsoft Word, Microsoft Edge, Notepad, LibreOffice, Firefox, and Adobe InDesign. There may be some settings which must be modified in order for the font to work. For example, in Microsoft Word, go to the <strong>Font / Advanced</strong> menu and select <strong>Ligatures / All</strong>. In Adobe InDesign, select <strong>Paragraph / Adobe World-Ready Paragraph Composer</strong>.

Mingzat follows the Unicode syllable order: C(.)(R)(Y)(V)(F)(^). This translates into Consonant (C) followed by optional nukta (.), followed by optional Ra (R), followed by optional Ya (Y), followed by optional dependent Vowel (V), followed by optional Final consonant sign (F), followed by optional Ran (^). If this structure is followed, and your application supports proper rendering, the font will display them in the correct order. Sample nonsense syllable:

<a href="https://software.sil.org/wp/wp-content/uploads/2019/03/syll.jpg"><img class="alignleft size-large wp-image-3109" src="https://software.sil.org/wp/wp-content/uploads/2019/03/syll-1024x116.jpg" alt="Lepcha nonsense syllable" /></a>

Mingzat is designed to work with OpenType. To take advantage of the advanced typographic capabilities of this font, you must be using applications that provide an adequate level of support for OpenType.

The font has been tested in Microsoft Word, Notepad, LibreOffice, and Adobe InDesign. It also works in Microsoft Edge and Firefox.

<h3>Data Conversion</h3>

A compiled and uncompiled TECkit <a href="https://github.com/silnrsi/wsresources/tree/master/scripts/Lepc/legacy/jg-lepcha/mappings" title="" class="external">conversion table</a> can be downloaded which maps data using the <strong>JG Lepcha font to Unicode</strong>. This map can be used with <a href="https://software.sil.org/teckit/" title="" class="external">TECkit</a> and/or <a href="https://software.sil.org/silconverters/" title="" class="external">SILConverters</a>. It has been minimally tested.

<h3>Keyboarding</h3>

Mingzat can be used with any Unicode Lepcha keyboarding program. The <a href="https://keyman.com/keyboards/sil_lepcha" title="" class="external">Lepcha (SIL) keyboard</a> for Linux, MacOS, Windows, and mobile devices is based on a phonetic representation of the script.

<h3 id="downloads">Downloads</h3>

<h4>License</h4>

This font is licensed under the <a href="https://openfontlicense.org/" title="" class="external">SIL Open Font License (OFL)</a>.

<h3>Font</h3>

[sil_download style="table" sort="name" where="info.type == 'font'"]

<h3>Release Notes for Version 1.200</h3>

<ul>
<li>Fixed positioning of LEPCHA SIGN RAN above LEPCHA VOWEL SIGN OO in OpenType</li>
<li>Fixed positioning of LEPCHA CONSONANT SIGN NYIN-DO in Opentype for combinations considered non-valid</li>
<li>Removed Graphite support</li>
</ul>

<h4>Known issues</h4>

No known issues.

<h3>Previous versions</h3>

[sil_download style="table" sort="name" where="info.type == 'prev font'"]

<h3>Mingzat version 1.100</h3>

<ul>
<li>Update fs bit to 7</li>
<li>Update advanced width of U+00A0 NO-BREAK SPACE to match U+0020 SPACE</li>
<li>Update advanced width of U+2008 PUNCTUATION SPACE to match U+002E FULL STOP</li>
<li>Added visible square box to .notdef</li>
</ul>

<h3>Mingzat version 1.000</h3>

<ul>
<li>Move font to new build system</li>
<li>Update OpenType because modern computers now support the Lepcha script</li>
<li>Update Graphite to fix issue with reordering</li>
<li>Add Latin characters to support <a href="https://github.com/silnrsi/pysilfont/blob/master/src/silfont/data/" title="" class="external">Recommended characters for Non-Roman fonts</a></li>
</ul>

[top]

<h3 id="contact">Source Code</h3>

Mingzat is licensed according to the terms of the SIL Open Font License. The latest source files are available in a <a href="https://github.com/silnrsi/font-mingzat/" title="" class="external">Github project</a>.

[top]

<h3 id="support">Support</h3>

These fonts are provided at no cost; however, they are expensive to produce and maintain. Please consider donating to SIL’s font development efforts to support future development. Go to <a href="https://give.sil.org/give/485238">SIL’s Give Direct page</a>. <strong>Thank you!</strong>


we are unable to provide a commercial level of personal technical support. We will, however, try to resolve problems that are reported to us. We do hope that you will report problems so they can be addressed in future releases. Even if you are not having any specific problems, but have an idea on how this system could be improved, we want to hear your ideas and suggestions. These problems or suggestions can be reported to us through creating an issue on the <a href="https://github.com/silnrsi/font-mingzat/issues" title="" class="external">Github project</a>. 


[top]

<h3 id="contact">Contact</h3>

General troubleshooting information, including frequently asked questions, can be found in the documentation. Additional information is also available on the general <a href="https://software.sil.org/fonts/guides" title="" class="external">Font Help Guides</a> page. If that fails to answer your question, send an email via this contact form.

Before requesting technical support, please:

<ul>
<li>Carefully read all the documentation provided with the font and on this site.</li>
<li>Please see our <a href="https://software.sil.org/fonts/guides">Font Help Guides</a>.</li>
</ul>

<h3>Language Software Community</h3>

<a class="external" href="https://community.software.sil.org/c/silfonts"><img class="lsc" title="Go to Language Software Community for SIL Fonts »" src="/wp/wp-content/uploads/2017/02/LSC_icon_80x80.png" /></a>

<p class="lsc">Support from other software users may be available through the <a class="external" href="//community.software.sil.org/c/silfonts">SIL Language Software Community</a>. This community will be growing to become the major source of software support.</p>

If that fails to answer your question, or you have a bug report, feature suggestion, or need help using the software, please contact us using the form below.

<hr />

[contact-form-7 id="408" title="WSTech Products Contact Form"]

[top]
