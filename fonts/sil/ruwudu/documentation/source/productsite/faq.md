
Many questions can be answered by consulting the following FAQ pages. Here are a few sample questions answered in each FAQ:

- [SIL fonts in general](http://software.sil.org/fonts/faq)
    - *How can I type...?*
    - *How can I use font features?*
    - *Will you add support for character...?*
    - *Will you add support for script...?*
    - *WIll you help me...?*

- [The SIL Open Font License (OFL-FAQ)](https://scripts.sil.org/OFL-FAQ_web)
    - *Can I use this font for...?*
    - *Can I modify the font and then include it in...*
    - *If I use the font on a web page do I have to include an acknowledgement?*
    - The full OFL-FAQ.txt is also included in the font package.

A generic FAQ for all of our Arabic scripts fonts can be found here: [Arabic Fonts - FAQ](http://software.sil.org/arabicfonts/support/faq/). FAQ's specific to Ruwudu are found below.

### *Where does the name Ruwudu come from?*

Ruwudu is the Manga word for "writing". This style of writing is used by the Manga people in Niger, West Africa. 

### *I used **Alkalami Light** which included a hacked encoding. What are the codepoints I should convert from and to?*

If you used **Alkalami Light**, we made some decisions which were unfortunately not Unicode compliant. Since the initial release of that font, many of these non Unicode compliant characters have been added to Unicode. You will need to re-encode some characters to be fully Unicode compliant. A chart which includes the list of characters is found at the bottom of the [Font Features](features) page.

These non Unicode compliant solutions were removed in v2.000 of **Ruwudu**.

### Problems with Bold weights

#### *Why does my application not show the Bold weight in font menus and dialogs?*

Some applications will list all the weights but leave out Bold. To access the Bold you need to choose Regular and turn on Bold using the application's UI controls such as a "B" button.

#### *Why do I sometimes get a fake Bold?*

If you choose a weight other than Regular (such as Medium), then use application controls to turn on Bold, some applications will make a "fake" Bold rather than use one of the real ones in the font (Medium, SemiBold, Bold). This is because only Regular has an associated Bold counterpart. This is a technical limitation with some apps and OSes. If you are using some other weight than Regular for text and want to make a word or phrase stand out you will need to select the text and apply one of the heavier weights manually. 

### *What characters are included with this release?*

See [Character Set Support](charset) for the full listing.

#### *I notice that Ruwudu is missing a number of characters that I would like. Will you add these?*

It is impossible for us to add every glyph that every person desires, but we do place a high priority on adding complete coverage of all the characters defined in Unicode for this Kano style of Arabic script use (excluding the Arabic Presentation Forms blocks, which are not recommended for normal use). You can send us your requests, but please understand that we are unlikely to add symbols where the user base is very small, unless they have been accepted into Unicode.

