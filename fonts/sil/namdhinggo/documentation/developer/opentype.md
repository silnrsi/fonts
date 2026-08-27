# OpenType

Some notes about the history of the OpenType code in this font.

This lookup was originally called IEO (as it's referred to in the comment) and originally included the imatra. The comment in the IkarK GSUB rule also states that the Ikar+Kemphreng ligature is positioned via the IEO rule. My notes contain the following explanation as to why ikar handling was removed from the lookup:

"Was having trouble getting the spacing right on a consonant followed by ikar. The next consonant was being positioned next to the consonant that had the ikar, rather than after the ikar. The ikar was defined as a mark, and had width (425 units) but it seemed that the advance width of the ikar was not being taken into account. Bob H explained that Uniscribe discards the width of any character defined as a combining mark if it is involved in any kind of lookup. The solution was to define ikar as 'simple' rather than 'mark', and remove it from the IEO lookup (and rename the lookup to EO)."

So it seems that the comment was not updated to reflect the change in our handling of the imatra. It may be that the USE behaves differently from Uniscribe in this regard, but a quick test in Notepad indicates that the font works OK as is so I think we can leave the imatra out of the lookup.

All this worked for many years (HB, DW, CT) except for the World Ready Composer (WRC) in Adobe InDesign (tested with 2026 which is v21.x). It seems that the WRC (that is, with HarfBuzz disabled) was assigning zero width to the ikar (after all U+1921 LIMBU VOWEL SIGN I has a general category of Mn), even thought it was classified as a base character in GDEF and was not being used in a lookup.

The ikar has been made into a mark again (with zero width). To get the correct shaping, there is now a GPOS rule to add the needed width to the ikar. All four of the mentioned shaping engines now shape correctly.

Later, it was discovered the the mukphreng had the same issues as the ikar. The same fix (as for the ikar) was applied.
