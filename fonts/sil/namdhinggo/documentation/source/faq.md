---
title: Namdhinggo - Frequently Asked Questions
fontversion: 3.200
---

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

### Problems with Bold weights

For more details on the issue with Bold weights see [Using Axis-Based Font Families](https://software.sil.org/fonts/axis-based-fonts/).

#### *Why does my application not show the Bold weight in font menus and dialogs?*

Some applications will list all the weights but leave out Bold. To access the Bold you need to choose Regular and turn on Bold using the application's UI controls such as a "B" button.

#### *Why do I sometimes get a fake Bold?*

If you choose a weight other than Regular (such as Medium), then use application controls to turn on Bold, some applications will make a "fake" Bold rather than use one of the real ones in the font (SemiBold, Bold, ExtraBold). This is because only Regular has an associated Bold counterpart. This is a technical limitation with some apps and OSes. If you are using some other weight than Regular for text and want to make a word or phrase stand out you will need to select the text and apply one of the heavier weights manually.

### *Why does the font not work in Microsoft Word?*

Microsoft needed to fix a [bug that affected Limbu script fonts](https://github.com/notofonts/limbu/issues/3), such as Namdhinggo. This fix is not available in Windows 10, but is present in Windows 11. Note that Microsoft fixed a part of Windows called DirectWrite, which is used by Microsoft Word on Windows for text shaping. Many applications, even on Windows, use HarfBuzz for text shaping.

### *Why does the font not work in applications using HarfBuzz?*

The bug in Windows also affected applications using [HarfBuzz](https://harfbuzz.github.io/) (such as Firefox, Chrome, Android, and LibreOffice) and [InDesign](https://writingsystems.info/topics/fonts/testing-shaping-engines/#indesign) (2020 and later) for text shaping. Versions of Namdhinggo before 3.200 [avoided](https://github.com/silnrsi/font-namdhinggo/commit/c9f4398dcf320a9c3a8f8a8e933311e64a69093e) this [bug](https://writingsystems.info/topics/fonts/testing-shaping-engines/#script-tags-and-the-use). Namdhinggo version 3.200 and later should work provided that the system has a fixed version of HarfBuzz (which is very likely since HarfBuzz fixed the issue a while ago).
