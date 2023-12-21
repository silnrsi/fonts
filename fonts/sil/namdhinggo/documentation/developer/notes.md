# Notes

From a Readme file that describes the hacks I used to get things to work, since Limbu script was not supported in any renderer back then. Note that although there's a note regarding Version 1006 (Jan 2015), that version was never distributed. The version on the SIL Software Namdhinggo site is 1.004. I believe the version in the github repo is 1.006 but the OpenType code was never put into it.

## 5 May 2009

Due to the lack of explicit support for Limbu in any of the major rendering engines (Uniscribe, ICU or Adobe) the Namdhinggo font has had to resort to kludgy hacks in order to work. Furthermore, the different rendering engines work in different ways, so the hacks needed depend on the rendering engine, which means we have to know which rendering engine is being used in order to produce a font that works with it.

Therefore, we have decided for now to produce a font which only works with Uniscribe. My first attempts, using script tag 'limb' were fruitless, presumably because Uniscribe doesn't have a Limbu shaping engine, so none of the lookups under 'limb' were being executed. At Peter Constable's suggestion I associated my lookups with the 'latn' script tag, in the hopes that they would be applied. That seems to have worked. My hacks are:

1. For the compound vowel signs oo and au (1925 and 1926) we want to be able to get at the two parts independently so we can position the top part over the base character. We do this by means of a decomposition rule uni1925 -> uni1920 uni1923 (and similarly for uni1926). Then the top part automatically gets positioned properly on the base character via the positioning rule for 1920.

2. If the compound vowel signs oo or au are followed by the length marker (kemphreng, 193A) the kemphreng goes on the top part of the vowel. This means we want to reorder the right half of the vowel and kemphreng so that the kemphreng comes between the two parts of the vowel. Reordering is usually done in the shaping engine, but since we don't have a shaping engine we have to do it with a substitution. But VOLT doesn't allow a many-to-many substitution, so we first use a ccmp to combine 1923 and 193A into a single glyph (the vowel has already been split into its component parts, so the right half is available as 1923), and then we deccompose that single glyph into the reverse order 193A, 1923. If VOLT allowed a substitution of the form '1923 193A -> 193A 1923' we wouldn't have to do it in two steps.

3. A similar process is done when a glide (subjoined ya 1929, ra 192A or wa 192B) comes between a base consonant and a vowel. The vowel needs to be positioned over the base consonant, so we need to reorder. So we do the same 'compose/decompose in a different order' trick, to get the vowel (possibly with kemphreng) next to the base consonant.

With these hacks, the font displays OK using straight Uniscribe. (Other renderers behave differently). But some applications don't display properly even though they use Uniscribe. In particular, Word tries to be clever and does some additional processing of its own which "breaks" our wonderful hacks. Thus, this font really only works in Notepad and other no-frills plain-text editors that use Uniscribe. In other applications (including those that use the ICU rendering engine) the basic text will display OK, but alignment of certain diacritics will be off.

Distributed version is "NamdhinggoSIL1004 OT 03.ttf".

## Addition, Feb 2014

In Windows 7, it doesn't display properly even in Notepad. Maybe the newer versions of Uniscribe are smarter, and don't apply 'latn' features to non-Latin text?

## Version 1006, Jan 2015

A new version was created in FontLab, adding glyphs for dotted circle (U+25CC) and the two new Limbu characters added in Unicode 7: Letter Gyan (191D) and Letter Tra (191E). This font is called "NamSIL1006.ttf".
