
Many questions can be answered by consulting the following FAQ pages. Here are a few sample questions answered in each FAQ:

- [SIL fonts in general](https://software.sil.org/fonts/faq)
    - *How can I type...?*
    - *How can I use font features?*
    - *Will you add support for character...?*
    - *Will you add support for script...?*
    - *WIll you help me...?*

- [The SIL Open Font License (OFL-FAQ)](https://openfontlicense.org/ofl-faq/)
    - *Can I use this font for...?*
    - *Can I modify the font and then include it in...*
    - *If I use the font on a web page do I have to include an acknowledgement?*
    - The full OFL-FAQ.txt is also included in the font package.
    
#### Where does the name Busra come from?

A popular tourist attraction, the Bou Sra waterfall is located in Bousra Eco Park in Mondulkiri Province, Cambodia. The name is also spelled Bu Sra, Bousra or Busra. It is famous for its triple-tier cascade.

#### How is this font different from the Khmer Busra font available as part of the older Mondulkiri font package?

There are significant differences between this Busra font and the previous version (7.100). A few of these are:

- The name of the font has changed from “Khmer Busra” to “Busra”. This allows both versions of the font to be installed simultaneously.
- The font supports a new Khmer encoding structure; see [UTN #61: Khmer Encoding Structure]( https://www.unicode.org/notes/tn61).
- There is no longer support for Graphite or Apple's AAT technology.
- The Latin has been completely redesigned.
- Oblique (italic) weights are not included. These will be provided in a later version.

### Problems with Bold weights

#### *Why does my application not show the Bold weight in font menus and dialogs?*

Some applications will list all the weights but leave out Bold. To access the Bold you need to choose Regular and turn on Bold using the application's UI controls such as a "B" button. See our [Font Help Guide on Axis-Based Font Families](https://software.sil.org/fonts/axis-based-fonts/) for more information.

#### *Why do I sometimes get a fake Bold?*

If you choose a weight other than Regular (such as ExtraLight), and then use application controls to turn on Bold, some applications will make a "fake" Bold rather than use one of the real ones in the font (Medium, SemiBold, Bold). This is because only Regular has an associated Bold counterpart. This is a technical limitation with some apps and OSes. If you are using a weight other than Regular for text and want to make a word or phrase stand out, you will need to select the text and apply one of the heavier weights manually. See our [Font Help Guide on Axis-Based Font Families](https://software.sil.org/fonts/axis-based-fonts/) for more information.
