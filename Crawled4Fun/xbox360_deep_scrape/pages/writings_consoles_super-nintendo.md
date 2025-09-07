# Super Nintendo / Famicom Architecture | A Practical Analysis

**Source:** https://www.copetti.org/writings/consoles/super-nintendo

[Home](https://www.copetti.org/)
[Consoles](https://www.copetti.org/writings/consoles/)
[About](https://www.copetti.org/about/)
[Support](https://www.copetti.org/support/)
# Super Nintendo / Famicom Architecture
## A practical analysis by Rodrigo Copetti
[](https://github.com/flipacholas/Architecture-of-consoles)[](https://crowdin.com/project/architecture-of-consoles)[](https://www.copetti.org/writings/consoles/materials/readings/)[](https://www.copetti.org/writings/consoles/super-nintendo)
If you use accessibility tools or old browsers, [switch to the ‘classic’ edition](https://classic.copetti.org/writings/consoles/super-nintendo/).
🇬🇧 - English 🇪🇸 - Español 🇧🇷 - Português (Brasil) 🇨🇳 - 简体字 👋 - Add translation
* * *
Book edition
[![eBook edition](https://www.copetti.org/images/consoles/_covers/en/super-nintendo_hu_27f0f267774599e9.jpg)](https://www.copetti.org/writings/consoles/materials/book/)
This article is also published in many bookstores for the benefit of offline readers. The eBooks are DRM-free, while the printed editions compile multiple articles and feature original photography at full resolution.
You can find printed compilations [here](https://www.amazon.com/dp/B0F4P5RB25?binding=paperback), and individual eBooks at [Amazon Kindle](https://www.amazon.com/dp/B0B5VM3NHS), [Apple Books](https://books.apple.com/us/author/rodrigo-copetti/id1632545359?see-all=books), [Kobo](https://www.kobo.com/us/en/search?query=Architecture+of+Consoles%3a+A+Practical+Analysis&fcsearchfield=Series&seriesId=7e46f843-4aee-53b4-97c2-82782e951af5) and [other stores](https://www.copetti.org/writings/consoles/materials/book/). The proceeds support the improvement of current articles and the development of new ones.
For more information, please take a look at [here](https://www.copetti.org/writings/consoles/materials/book/).
* * *
Table of Contents
  1. [Supporting imagery](https://www.copetti.org/writings/consoles/super-nintendo#imagery)
  2. [A quick introduction](https://www.copetti.org/writings/consoles/super-nintendo#a-quick-introduction)
    1. [Models and revisions](https://www.copetti.org/writings/consoles/super-nintendo#models-and-revisions)
  3. [CPU](https://www.copetti.org/writings/consoles/super-nintendo#cpu)
    1. [Modernising the 6502](https://www.copetti.org/writings/consoles/super-nintendo#modernising-the-6502)
    2. [The new CPU](https://www.copetti.org/writings/consoles/super-nintendo#the-new-cpu)
    3. [Ricoh’s additions](https://www.copetti.org/writings/consoles/super-nintendo#ricohs-additions)
      1. [Speedy memory access](https://www.copetti.org/writings/consoles/super-nintendo#speedy-memory-access)
      2. [The 16-bit Segmentation Fault](https://www.copetti.org/writings/consoles/super-nintendo#the-16-bit-segmentation-fault)
    4. [(Lots of) more memory](https://www.copetti.org/writings/consoles/super-nintendo#lots-of-more-memory)
  4. [Graphics](https://www.copetti.org/writings/consoles/super-nintendo#graphics)
    1. [Design](https://www.copetti.org/writings/consoles/super-nintendo#design)
      1. [The chipset](https://www.copetti.org/writings/consoles/super-nintendo#the-chipset)
      2. [Display modalities](https://www.copetti.org/writings/consoles/super-nintendo#display-modalities)
    2. [Organising the content](https://www.copetti.org/writings/consoles/super-nintendo#organising-the-content)
    3. [Constructing the frame](https://www.copetti.org/writings/consoles/super-nintendo#constructing-the-frame)
      1. [Tiles](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-1-tiles)
      2. [Background](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-2-background)
      3. [Modes](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-3-modes)
      4. [Sprites](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-4-sprites)
      5. [Result](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-5-result)
    4. [That feature](https://www.copetti.org/writings/consoles/super-nintendo#that-feature)
      1. [Generous circuits](https://www.copetti.org/writings/consoles/super-nintendo#generous-circuits)
    5. [More colour magic](https://www.copetti.org/writings/consoles/super-nintendo#more-colour-magic)
    6. [Cause of frame drops](https://www.copetti.org/writings/consoles/super-nintendo#cause-of-frame-drops)
    7. [A convenient video out](https://www.copetti.org/writings/consoles/super-nintendo#a-convenient-video-out)
  5. [Audio](https://www.copetti.org/writings/consoles/super-nintendo#audio)
    1. [Architecture](https://www.copetti.org/writings/consoles/super-nintendo#architecture)
    2. [Pitch control](https://www.copetti.org/writings/consoles/super-nintendo#pitch-control)
    3. [Evolution from the NES](https://www.copetti.org/writings/consoles/super-nintendo#evolution-from-the-nes)
    4. [Advanced usage](https://www.copetti.org/writings/consoles/super-nintendo#advanced-usage)
    5. [Stereo confusion](https://www.copetti.org/writings/consoles/super-nintendo#stereo-confusion)
  6. [Games](https://www.copetti.org/writings/consoles/super-nintendo#games)
    1. [Cartridge configuration](https://www.copetti.org/writings/consoles/super-nintendo#cartridge-configuration)
      1. [Beyond convention](https://www.copetti.org/writings/consoles/super-nintendo#beyond-convention)
  7. [Anti-piracy / Region Lock](https://www.copetti.org/writings/consoles/super-nintendo#anti-piracy-region-lock)
  8. [That’s all folks](https://www.copetti.org/writings/consoles/super-nintendo#thats-all-folks)
  9. [Copyright and permissions](https://www.copetti.org/writings/consoles/super-nintendo#referencing)
  10. [Sources / Keep Reading](https://www.copetti.org/writings/consoles/super-nintendo#sources)
  11. [Contributing](https://www.copetti.org/writings/consoles/super-nintendo#contributing)
  12. [Changelog](https://www.copetti.org/writings/consoles/super-nintendo#changelog)


* * *
## Supporting imagery
  * [Model](https://www.copetti.org/writings/consoles/super-nintendo#cover-model)
  * [Motherboard](https://www.copetti.org/writings/consoles/super-nintendo#cover-motherboard)
  * [Diagram](https://www.copetti.org/writings/consoles/super-nintendo#cover-diagram)


### Model
  * [International](https://www.copetti.org/writings/consoles/super-nintendo#cover-model-international)
  * [American](https://www.copetti.org/writings/consoles/super-nintendo#cover-model-american)

[![International](https://www.copetti.org/images/consoles/snes/international.c1c3e550ebb7eceeb5713c069ab271bec1241cf33f788ff0fdf697be2a1ee8e2.png)](https://www.copetti.org/images/consoles/snes/international.c1c3e550ebb7eceeb5713c069ab271bec1241cf33f788ff0fdf697be2a1ee8e2.png)The Super Nintendo (in Europe) or Super Famicom (in Japan).  
Released on 21/11/1990 in Japan and 11/04/1992 in Europe.[![American](https://www.copetti.org/images/consoles/snes/american.6edc51997e083e243106da07293c4246378e0f2a51acfe71d36332782d29f2e8.png)](https://www.copetti.org/images/consoles/snes/american.6edc51997e083e243106da07293c4246378e0f2a51acfe71d36332782d29f2e8.png)The Super Nintendo.  
Released on 13/08/1991 in America.
### Motherboard
  * [Original](https://www.copetti.org/writings/consoles/super-nintendo#cover-motherboard-original)
  * [Marked](https://www.copetti.org/writings/consoles/super-nintendo#cover-motherboard-marked)

[![Motherboard](https://www.copetti.org/images/consoles/snes/motherboard.db42e7004b4b1d51bc74ffb313b04d76879ee41405b7d4578c9f7ddb4b322a18.jpg)](https://www.copetti.org/images/consoles/snes/motherboard.db42e7004b4b1d51bc74ffb313b04d76879ee41405b7d4578c9f7ddb4b322a18.jpg)Motherboard  
Showing revision 'SNS-RGB-CPU-01'.  
Earlier revisions had the Sound Subsystem connected as a daughterboard, later ones unified both PPUs.[![Motherboard](https://www.copetti.org/images/consoles/snes/motherboard_marked.17336739259232e906c602b3fe447680ac09af977ed8e4e93342cbb7d8652c70.jpg)](https://www.copetti.org/images/consoles/snes/motherboard_marked.17336739259232e906c602b3fe447680ac09af977ed8e4e93342cbb7d8652c70.jpg)Motherboard with important parts labelled
### Diagram
[![Diagram](https://www.copetti.org/images/consoles/snes/_diagrams/main.c778fdab7eab327bc7b66642b7fbee4127e070840e60e072fe4114bdf2e450a4.png)](https://www.copetti.org/images/consoles/snes/_diagrams/main.c778fdab7eab327bc7b66642b7fbee4127e070840e60e072fe4114bdf2e450a4.png)Main architecture diagram  
Bus 'A' and 'B' are address buses, the data bus follows the trail of bus 'B' and it's 8 bits wide.
* * *
## A quick introduction
It seems Nintendo managed to deliver the next generation of graphics and sound without using expensive off-the-shelf components. But there’s a catch: the new console was also **designed with expandability in mind**. In a world where CPUs are evolving faster than the speed of light, Nintendo ultimately relied on game cartridges to make its console shine.
### Models and revisions
Kids across the globe saw this console in various shapes, colours, and names. Nevertheless, the internal differences were less noticeable. As you may already know, due to the spread of analogue standards, models from different regions exhibit variations in their analogue signals (e.g., video output) to accommodate these differing standards. Compared to [its predecessor](https://www.copetti.org/writings/consoles/nes/), however, the architectural differences are less pronounced. For instance, on this occasion, Nintendo did not include exclusive circuitry for [audio expansion](https://www.copetti.org/writings/consoles/nes/#tab-4-1-extra-channels), which significantly impacted the quality of games across regions.
The company did ship hardware revisions during its lifespan, but their main purpose was to reduce the number of dedicated components on the motherboard, thereby lowering manufacturing cost.
* * *
## CPU
The Super Nintendo’s choice of processor is a peculiar one. Unlike [its competition](https://www.copetti.org/writings/consoles/mega-drive-genesis/#cpu) bundling a fully-fledged 68000, the SNES’ chip is not a radical departure from its predecessor. To recap, the NES employed a [modified 6502](https://www.copetti.org/writings/consoles/nes/#core-functionality) CPU, an admired ingredient of late-70s and early-80s computers. Now, to pave the way for the new decade (the 90s), Nintendo opted for a more conservative (and cheaper) solution: the **WDC 65C816** , a 16-bit extension of the 6502.
### Modernising the 6502
The 65C816 CPU originates from Western Design Center (WDC), particularly from Bill Mensch, a former member of the 6502 team (at MOS) and the 6800 team (at Motorola). In 1978, one year after leaving MOS, Mensch founded Western Design Center, a semiconductor company that produces clones of the MOS 6502 with attractive enhancements (e.g., CMOS design, extra opcodes, circuitry fixes, new addressing modes, etc.).
[![Image](https://www.copetti.org/images/consoles/snes/photos/65816.2c626df9a08ff50a5bb5509d4b35c26402693167d072c139d1a422c2560d8be5_hu_59d2b72902e53351.png)](https://www.copetti.org/images/consoles/snes/photos/65816.2c626df9a08ff50a5bb5509d4b35c26402693167d072c139d1a422c2560d8be5.webp)The WDC 65C816 chip found on the Apple IIGS.
One day, Apple approached WDC to design a backwards-compatible variant of the 6502 that could process larger amounts of data. This resulted in the WDC 65C816 CPU, released in 1983. Curiously enough, Apple encountered many setbacks during the development of a computer that would use the new CPU, until three years later, with the release of the Apple IIGS.
[![Image](https://www.copetti.org/images/consoles/snes/photos/wdcstack.d41a90757876b0e67521e284b167ce48a6888dc12f26300f6fbb818fcd84f1e1_hu_9548022374923e72.png)](https://www.copetti.org/images/consoles/snes/photos/wdcstack.d41a90757876b0e67521e284b167ce48a6888dc12f26300f6fbb818fcd84f1e1.webp)In the end, the Apple IIGS and the Super Nintendo became the only major adopters of the 65C816 CPU.
Meanwhile, Nintendo was enjoying a good relationship with Ricoh and their set of bespoke chips for the NES. I haven’t found the exact document outlining what connected Ricoh to WDC, but what I can confirm is that at some point in time, WDC agreed to license their 65C816 designs to Ricoh [[1]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-interview). Consequently, the latter tailored it to meet the new requirements of the Super Nintendo, it became the **Ricoh 5A22** and was exclusively supplied to Nintendo.
### The new CPU
As you’ve seen before, the main processor of this console is the **Ricoh 5A22** , a superset of the 65C816.
[![Image](https://www.copetti.org/images/consoles/snes/photos/s-cpu.282d88e4761530efe8344c49af67d947eb9d1ebea15f09cb210a0af5e0d47511_hu_a0b0f9ede7610390.png)](https://www.copetti.org/images/consoles/snes/photos/s-cpu.282d88e4761530efe8344c49af67d947eb9d1ebea15f09cb210a0af5e0d47511.webp)The Ricoh 5A22 chip, labelled ‘S-CPU’ by Nintendo.
Unlike the Apple IIGS, which enjoyed backward compatibility with Apple II software, the Super Nintendo is **not compatible with NES games**. To be fair, based on the choice of processor, there’s a slight possibility that the SNES was originally planned to be compatible with NES games, who knows.
Moving on, the CPU employs a **variable clock speed** , reaching up to **3.58 MHz** for register operations and dropping to **1.79 MHz** when accessing the slowest buses (i.e. the serial/controller port).
Now, to properly understand the functionality of the 5A22, we must first look at what the 65C816 provides:
  * The **65816 ISA** : The debut 16-bit instruction set of the 65C816. It is based on the 6502 ISA but does not implement undocumented instructions that some NES games resorted to [[2]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-unoffopcodes).
    * The size of instructions can vary between 1 byte (8 bits) and 4 bytes (32 bits), depending on how memory addresses are referenced (a.k.a. the ‘addressing mode’ used) [[3]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-isaref).
    * The [broken BCD mode](https://www.copetti.org/writings/consoles/nes/#scrapped-functions) is **functional** again (I’m guessing as a consequence of _appropriate_ licensing).
  * **10 different modes of operation** : Due to a combination of backwards compatibility with the 6502, the return of the BCD mode (missing on the NES), and the ability to switch between groups of 16-bit and 8-bit registers [[4]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-opcodes), developers can utilise this CPU using different combinations of these.
    * Unlike later [MIPS CPUs](https://www.copetti.org/writings/consoles/nintendo-64/#cpu), there isn’t a mixed instruction set with dedicated opcodes for 8-bit and 16-bit words. Instead, the same instruction set is interpreted differently depending on the mode activated.
    * For compatibility reasons, the CPU always starts in ‘emulation’ mode (pure 6502), and it is up to the program to switch to a particular ‘native’ mode to enable 16-bit functionality. On a side note, it is amusing how Intel’s x86 still follows the [same modus operandi](https://www.copetti.org/writings/consoles/xbox/#boot-process) in their modern CPUs.
  * **Three 16-bit general-purpose registers**. This set matches the 6502’s (`X`, `Y` and `A`). However, due to the different modes of operation, these registers can now switch between 16-bit and 8-bit.
    * Compare this number to the [sixteen 32-bit registers](https://www.copetti.org/writings/consoles/mega-drive-genesis/#the-leader) the competition offered - quite a contrast!
  * **16-bit internal data bus** and an **8-bit external data bus** : This results in performance penalties when moving values larger than 8 bits across memory (as the CPU requires additional cycles), a common occurrence considering most instructions are 16-bit long. However, the overall impact is alleviated thanks to Ricoh’s DMA units (explained later on) and the variable clock speed.
  * **24-bit address space** : Allows the CPU to access **up to 16 MB worth of memory**. This is similar to the [Motorola 68000](https://www.copetti.org/writings/consoles/mega-drive-genesis/#cpu), except the 65C816 obtains its 24-bit addresses by combining extra 8-bit registers (`DBR` and `PBR`) with the original 16-bit addressing lines of the 6502 [[5]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-chibi). Overall, this methodology is similar to housing an [internal mapper](https://www.copetti.org/writings/consoles/pc-engine/#memory-access).


Looking at this, I have to confess that the 65C816 feels excessively cumbersome for little gain. Compared to other offerings such as the [Motorola 68000](https://www.copetti.org/writings/consoles/mega-drive-genesis/#the-leader), it is not difficult to conclude why the Apple IIGS remained the only personal computer to adopt the 65C816. Nonetheless, throughout this article, you will see how Nintendo and Ricoh managed to turn the limitations of this CPU into opportunities to revamp its game library.
### Ricoh’s additions
In 1983, the 65C816 CPU was conceived as a general-purpose successor of its 1975 ancestor, with all the associated requirements and constraints. Yet, Nintendo planned its console to last throughout the 90s, meaning Ricoh had to step up its game (if you’ll pardon the pun).
First on the list was tackling its arithmetic limitations - the 65C816 lacks dedicated instructions for multiplication or division. As a result, Ricoh incorporated **multiplication** and **division units** , enabling the CPU to perform these types of operations via hardware (rather of software). Instead of conventional instructions, they are operated through registers.
The multiplier receives 8-bit numbers and outputs 16-bit ones [[6]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-multiplication). Conversely, the divider takes a 16-bit dividend and an 8-bit divisor; and returns a 16-bit quotient along with a 16-bit remainder [[7]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-division). Both units only support positive numbers (called ‘unsigned’).
Now, you may be wondering ‘why is this relevant?’. The significance of these additions will become clear when we explore the novelties of the Super Nintendo’s graphics chips (in the ‘Graphics’ section).
#### Speedy memory access
The second challenge was to increase its data bandwidth. Hence, **two exclusive DMAs** (Direct Memory Access) were added to move data around without the intervention of the CPU, resulting in faster speeds. For this design to work, regions of memory are referenced using two distinct address buses [[8]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-manual):
  * A **24-bit ‘A Bus’** controlled by the CPU: Connects the cartridge, CPU, and WRAM.
  * A **8-bit ‘B Bus’** controlled by the S-PPU: Connects the cartridge, CPU, WRAM, S-PPU, and the Audio CPU.


When setting up a DMA transfer, the _origin_ bus must differ from the _destination_ bus.
Furthermore, the two DMAs are not identical and serve very distinct functions [[9]](https://www.copetti.org/writings/consoles/super-nintendo#bib:graphics-piepgrass):
  * The **General-Purpose DMA** performs transfers at any time, temporarily halting the CPU until the transfer is finished.
  * The **Horizontal DMA** (HDMA) performs a small transfer after each horizontal scan (while the CRT beam is preparing to draw the next row). This prevents prolonged CPU interruption, but transfers are limited to 4 bytes per scanline.


Finally, the system provides **eight channels** for DMA transfers, enabling to dispatch up to eight independent transfers at once.
#### The 16-bit Segmentation Fault
The primitive [Open Bus behaviour](https://www.copetti.org/writings/consoles/nes/#segmentation-fault) is also present in this console. Furthermore, there has been speculation about the existence of an internal register called **Memory Data Register** (MDR), which is believed to store such values [[10]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-mdr).
For comparison, the 68000 employs a vector table to handle exceptions, ensuring execution is redirected whenever a fault is detected.
### (Lots of) more memory
It’s fascinating to realise how much content the NES managed to display with only [2 KB of RAM](https://www.copetti.org/writings/consoles/nes/#memory). Well, the Super Nintendo now features **128 KB of SRAM** (still referred to as ‘Work RAM’ or WRAM) - a staggering 6400% increase in general-purpose memory compared to its predecessor.
So, what can developers do with this? Anything they desire, really. WRAM is used to store variable data for the game. The more space available, the greater the amount of information that can be stored and processed (thus, reducing reliance on [cartridge hardware](https://www.copetti.org/writings/consoles/nes/#cartridgegame-data)).
However, as the following sections will demonstrate, the Super Nintendo is a fairly complex machine (albeit its ‘simplistic’ CPU). I tend to call this console a ‘collection of mini-computers/subsystems’. Each subsystem may need data from the CPU, meaning programmers may reserve portions of WRAM to process that information - thus justifying the need for 128 KB of memory.
* * *
## Graphics
After everything discussed so far, let me tell you that the graphical subsystem of this console is a true feat of engineering. Given its constrained CPU, one might assume the SNES could never cast a shadow on [its competitor](https://www.copetti.org/writings/consoles/mega-drive-genesis/), which boasts a ‘32-bit’ Motorola 68000. Yet, Nintendo and Ricoh engineers devised clever tricks that exploit the behaviour of CRT displays, effectively expanding the console’s capabilities without the need for expensive, state-of-the-art components.
Before diving deeper into this topic, I strongly recommend reading the [NES article](https://www.copetti.org/writings/consoles/nes/#graphics) first, as it introduces key concepts that will be revisited here.
### Design
As with any other console of its generation, the Super Nintendo draws graphics using 2D tiles (8 x 8 pixels). The NES initially achieved this through it signature **Picture Processing Unit** (PPU), which beams the image in sync with a CRT screen. The Super Nintendo follows suit but incorporates more sophisticated techniques to obtain richer results.
#### The chipset
The Super Nintendo houses two different PPU chips that constitute the graphics subsystem, collectively known as the **Super PPU** or ‘S-PPU’.
[![Image](https://www.copetti.org/images/consoles/snes/photos/s-ppus.1a078ec0f83d4662b06c5cb66fdd4cee41e86110a227085e7ab175f5583338b7_hu_ba1736a7e1ac8fe3.png)](https://www.copetti.org/images/consoles/snes/photos/s-ppus.1a078ec0f83d4662b06c5cb66fdd4cee41e86110a227085e7ab175f5583338b7.webp)The two PPU chips.
Each PPU package serves specific functionality [[11]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-manual):
  * **PPU 1** : Renders graphics (tiles) and applies transformations such as rotation and scaling.
  * **PPU 2** : Provides visual effects, including windowing, mosaic, and fading, over the rendered graphics.


This separation, from a programming perspective, is redundant, as both chips are effectively treated as a single unit.
#### Display modalities
The NTSC system outputs a standard resolution of **256 x 224 pixels** at **~60 Hz** [[12]](https://www.copetti.org/writings/consoles/super-nintendo#bib:graphics-guide). The European variant, adhering to the PAL specification, outputs **256 × 240 pixels** at **~50 Hz**. Be as it may, most games do not utilise the additional pixels and instead display a _letterbox_ (black lines).
Now, here’s the tricky part: traditional TVs have an aspect ratio of 4:3. Yet, if you do the math, the Super Nintendo’s output resolution has an **aspect ratio of 8:7**. Consequently, once the image is beamed on the TV, it looks **horizontally stretched** , resembling a **292 x 224 pixels** frame instead (in the case of the NTSC variant) [[13]](https://www.copetti.org/writings/consoles/super-nintendo#bib:graphics-aspect). Put simply, pixels on the Super Nintendo have an aspect ratio of 8:7, rather than being ‘perfectly square’.
[![Image](https://www.copetti.org/images/consoles/snes/stretch/internal.484f9406c1812c4811b40c4a0a298d392b8b1c9a71d26706818f08364de7d41c.png)](https://www.copetti.org/images/consoles/snes/stretch/internal.484f9406c1812c4811b40c4a0a298d392b8b1c9a71d26706818f08364de7d41c.png)Rendered frame with a resolution of 256 x 224 pixels. This is what the console sends to the TV.[![Image](https://www.copetti.org/images/consoles/snes/stretch/external.efd80fb8d67220ae282be1a021ccbc7d3ee3c77b14b974527cbdfe14ad29f49d.png)](https://www.copetti.org/images/consoles/snes/stretch/external.efd80fb8d67220ae282be1a021ccbc7d3ee3c77b14b974527cbdfe14ad29f49d.png)Stretched frame as seen from the TV (with an apparent resolution of 292 x 224 pixels).Kirby’s Dream Land 3 (1997).
The reasoning behind Nintendo’s deviation from the standard aspect ratio boils down to **cost**. You will soon see that the S-PPU is very rich in functionality, but not fast enough to render everything at the pace of the CRT beam [[14]](https://www.copetti.org/writings/consoles/super-nintendo#bib:graphics-sanglard). Rather than adding more circuitry to the board, Nintendo opted to short the width of the visible image, allocating extra space for the horizontal blanking period instead.
Nevertheless, some games like ‘Chrono Trigger’ account for this factor by intentionally using squashed shapes, which then look correct after being stretched by the TV. This, however, remains an exception, since the majority of games take no extra measures to compensate for this effect.
### Organising the content
[![Image](https://www.copetti.org/images/consoles/snes/_diagrams/sppu.2d986b0dc1818d5e6c53382be5f665baeccf6eaeab684500392fa1f852a7bf7c.png)](https://www.copetti.org/images/consoles/snes/_diagrams/sppu.2d986b0dc1818d5e6c53382be5f665baeccf6eaeab684500392fa1f852a7bf7c.png)Memory architecture of the S-PPU.
Due to cost and performance reasons, graphics data is distributed across three memory regions:
  * 64 KB **VRAM** (Video RAM): Stores tiles and maps (tables) used to build background layers.
  * 512 B **CGRAM** (Colour Graphics RAM): Fits 512 colour palette entries, with each entry occupying a _word_ (16 bits).
  * 544 B **OAM** (Object Attribute Memory): Contains tables referencing 128 tiles that will be used as _sprites_ , along with their attributes.


VRAM is implemented using **two 32 KB chips** , each accessed simultaneously via a separate 8-bit bus. This allows the PPU 1 to fetch 16-bit values per cycle, making it particularly efficient for retrieving multiple consecutive pixels in real time [[15]](https://www.copetti.org/writings/consoles/super-nintendo#bib:graphics-sanglard_how). Additionally, each VRAM chip is connected to a dedicated 16-bit address bus, rather than a shared one. This will prove useful when the PPU 1 needs to switch to alternative memory arrangements - something we’ll explore in more detail when we talk about ‘Mode 7’.
### Constructing the frame
Let’s now see how a frame is rendered on the console and subsequently displayed on TV. For demonstration purposes, _Super Mario World_ will serve as example.
  * [Tiles](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-1-tiles)
  * [Background](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-2-background)
  * [Modes](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-3-modes)
  * [Sprites](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-4-sprites)
  * [Result](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-5-result)


#### Tiles
[![Image](https://www.copetti.org/images/consoles/snes/sppu_mario/tiles.09061e523e90dc67d4ef5d43480c7cd96135065344a0e30da88bf317fefebcf5.png)](https://www.copetti.org/images/consoles/snes/sppu_mario/tiles.09061e523e90dc67d4ef5d43480c7cd96135065344a0e30da88bf317fefebcf5.png)Some 16x16 Tiles found in VRAM.
Just like its predecessor, the S-PPU uses tiles to build sophisticated graphics. Although, there are significant improvements compared to the original PPU:
  * **Game cartridges are no longer wired to the PPU** , meaning tiles must first be copied to VRAM (similar to Sega’s [Mega Drive](https://www.copetti.org/writings/consoles/mega-drive-genesis/#graphics)). This is where the DMA unit becomes very handy.
  * **Tiles are no longer restricted to their traditional dimension** (8x8 pixels) - they can now be up to **16x16 pixels** wide.
  * When tiles are stored in memory, these are **compressed based on colour depth** (in other words, the number of colours per pixel). The unit of measurement for this is **bpp** (bits per pixel). The minimum value is **2 bpp** , meaning each pixel occupies two bits and has only 4 colours available. The maximum is **8 bpp** , allowing for 256 colours per pixel (at the expense of consuming a full byte of memory).


« Previous [Next »](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-2-background)
#### Background
  * [Layer 1](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-1-1-layer-1)
  * [Layer 2](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-1-2-layer-2)
  * [Layer 3](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-1-3-layer-3)

[![Image](https://www.copetti.org/images/consoles/snes/sppu_mario/background1_map.21df31b448cf23a9a35926ec5626b0c3f6d123399a560939acef6958bd751aae.png)](https://www.copetti.org/images/consoles/snes/sppu_mario/background1_map.21df31b448cf23a9a35926ec5626b0c3f6d123399a560939acef6958bd751aae.png)Background Layer 1 (BG1).[![Image](https://www.copetti.org/images/consoles/snes/sppu_mario/background2_map.bd5b815a8deee8c0bebf4b5cf2e83aa663acd9a42fd11f0a7849e1dbbaca2717.png)](https://www.copetti.org/images/consoles/snes/sppu_mario/background2_map.bd5b815a8deee8c0bebf4b5cf2e83aa663acd9a42fd11f0a7849e1dbbaca2717.png)Background Layer 2 (BG2).[![Image](https://www.copetti.org/images/consoles/snes/sppu_mario/background3_map.76cab3b532b04066ddb79819bdcf30b0ff80f9d589d43be554cc51093aff6a0b.png)](https://www.copetti.org/images/consoles/snes/sppu_mario/background3_map.76cab3b532b04066ddb79819bdcf30b0ff80f9d589d43be554cc51093aff6a0b.png)Background Layer 3 (BG3).Background maps in VRAM.
  * [Layer 1](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-2-1-layer-1)
  * [Layer 2](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-2-2-layer-2)
  * [Layer 3](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-2-3-layer-3)
  * [Combined](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-2-4-combined)

[![Image](https://www.copetti.org/images/consoles/snes/sppu_mario/background1.ef7af8ea012cc4307cf32d2bd54af8a885c2f5405ac2eb0f81d6a95d41a6c7df.png)](https://www.copetti.org/images/consoles/snes/sppu_mario/background1.ef7af8ea012cc4307cf32d2bd54af8a885c2f5405ac2eb0f81d6a95d41a6c7df.png)Rendered Background Layer 1 (BG1).[![Image](https://www.copetti.org/images/consoles/snes/sppu_mario/background2.c856a3affcca18dccd4822d838c5c11d365bd46b92c2de635bd2d8241517eeed.png)](https://www.copetti.org/images/consoles/snes/sppu_mario/background2.c856a3affcca18dccd4822d838c5c11d365bd46b92c2de635bd2d8241517eeed.png)Rendered Background Layer 2 (BG2).[![Image](https://www.copetti.org/images/consoles/snes/sppu_mario/background3.37432ac4ab6b07d188bb557c8bd35809cc85cb9ed6395dc8269a41afcb98b959.png)](https://www.copetti.org/images/consoles/snes/sppu_mario/background3.37432ac4ab6b07d188bb557c8bd35809cc85cb9ed6395dc8269a41afcb98b959.png)Rendered Background Layer 3 (BG3).[![Image](https://www.copetti.org/images/consoles/snes/sppu_mario/background_complete.b3128c1219030182304399a4e7b0475520f191548fa5bf7828a136bccb951aa6.png)](https://www.copetti.org/images/consoles/snes/sppu_mario/background_complete.b3128c1219030182304399a4e7b0475520f191548fa5bf7828a136bccb951aa6.png)Rendered Background Layers combined.Rendered Background layers after selection and transparency are applied.
The Super Nintendo can generate up to four different background planes. Using either 8x8 or 16x16 tiles, [blocks](https://www.copetti.org/writings/consoles/nes/#tab-1-2-background-layer) are made of 32x32 pixels (2x2 tiles). That being said, each background layer can extend up to 1024x1024 pixels in size (32x32 tiles). The region in VRAM where these layers are configured is called **Tilemap** , and is structured as a table (continuous values in memory).
Each Tilemap entry contains the following attributes:
  * Vertical and horizontal flip values.
  * Priority (either `0` or `1`).
  * Palette reference from CGRAM.
  * Tile reference.


As always, these planes are scrollable. However, the number of features available - such as colour depth, number of layers, independent scrolling regions, and size of selection - depends on the **Background Mode** activated on the S-PPU, which brings us to the next section…
[« Previous](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-1-tiles) [Next »](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-3-modes)
#### Modes
The S-PPU provides many operations for backgrounds, but these cannot be chosen arbitrarily. Instead, programmers must choose from **eight background modes** , each offering a distinct set of features [[16]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-rgme):
  * **Mode 0** : 4 layers with 4 colours each.
    * The colour palette is particularly bland, as this mode prioritises the highest number of layers.
  * **Mode 1** : 2 layers with 16 colours each + 1 layer with 4 colours.
    * One layer can be split into foreground and background.
    * This is the most commonly used mode.
  * **Mode 2** : 2 layers with 16 colours each.
    * There is an extra effect available: layers can have each of their columns scrolled independently (similarly to the [Game Boy wobble effect](https://www.copetti.org/writings/consoles/game-boy/#tab-2-1-wobble-effect) but applied vertically).
  * **Mode 3** : 1 layer with 256 colours + 1 layer with 16 colours.
    * Colours can be defined using RGB values instead of referencing CGRAM.
  * **Mode 4** : Mode 2 and 3 combined (Column scroll + RGB colour mapping).
    * The first layer supports 256 colours, while the second is limited to just 4 colours.
  * **Mode 5** : 1 layer with 16 colours + 1 layer with 4 colours.
    * The selected area features an outstanding resolution of **512 x 224 pixels** , which will be horizontally squashed to fit on the screen (the final output remains 256 x 224 pixels!). This comes at the cost of rendering 16 x 8 pixels tiles as 8 x 8 ones, and 16 x 16 pixels tiles as 8 x 16 ones.
    * Furthermore, the vertical resolution can be extended by activating **interlacing** , reaching **512 x 448 pixels** , which now maintains correct proportions with the output frame. In exchange, interlacing applies the same squashing effect to tiles - this time vertically. This is useful when displaying larger amounts of information (e.g. multiplayer or split-screen).
  * **Mode 6** : A combination of Mode 2 and 5 (high resolution + column scrolling), though it is restricted to a single layer with 32 colours.


As you can see, programmers can now decide whether to prioritise colour depth, number of layers, special effects, or resolution.
[« Previous](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-2-background) [Next »](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-4-sprites)
#### Sprites
[![Image](https://www.copetti.org/images/consoles/snes/sppu_mario/sprites.09a501844fa5bed712503a839eea3f67572fd1a7e05a17a1c26b42e47ebf57eb.png)](https://www.copetti.org/images/consoles/snes/sppu_mario/sprites.09a501844fa5bed712503a839eea3f67572fd1a7e05a17a1c26b42e47ebf57eb.png)Rendered Sprite layer.
A dedicated memory region called **Object Attribute Memory** (OAM) stores a table with references of up to 128 sprites, each with the following properties [[17]](https://www.copetti.org/writings/consoles/super-nintendo#bib:graphics-guidelines):
  * **Size** : The S-PPU can combine up to 16 tiles into a 4x4 tile quadrant to build a sprite.
  * **Tile references** : Specifies the tiles used to draw the sprite.
  * **Screen position** : Only sprites within the visible area will be rendered.
  * **Priority** : Since multiple layers overlap, the graphic with the highest priority will be shown. Priority is also determined by the background mode in use.
  * **Colour palette slot** : Allows selection from 9 palette slots in CGRAM.
  * **X/Y Flip** : Enables horizontal and vertical flipping.


The S-PPU can render **up to 32 sprites per scanline** ; overflowing this will only make the S-PPU discard the ones with the lowest priority.
[« Previous](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-3-modes) [Next »](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-5-result)
#### Result
[![Image](https://www.copetti.org/images/consoles/snes/sppu_mario/complete.93dee172d17a59a685885d2a5e222a1082a65df8268bbf0a13d05d091652a5b0.png)](https://www.copetti.org/images/consoles/snes/sppu_mario/complete.93dee172d17a59a685885d2a5e222a1082a65df8268bbf0a13d05d091652a5b0.png)Tada!
The S-PPU renders each scanline on-the-fly, first processing the relevant portion of each layer and then mixing them.
One of the key constraints of NES games was that graphical updates could only occur during **V-Blank** - the brief interval when the CRT beam was returning to the starting point provided a reasonable time frame to reshuffle some tiles without breaking the image.
Well, now thanks to the enhanced capabilities of the SNES, this limitation now takes on a different meaning.
You see, because the new DMA/HDMA units enable programmers to perform memory transfers without waiting for V-Blank [[18]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-dma), games can now update tiles, colours, and registers without waiting for the entire frame to be drawn. In fact, the possibilities extend even further: since games can now **modify S-PPU settings mid-frame** , it becomes possible to **activate different background modes at different stages within the same frame** , unlocking new and original game designs!
[« Previous](https://www.copetti.org/writings/consoles/super-nintendo#tab-1-4-sprites) Next »
### That feature
Truth to be told, I still haven’t mentioned the most important characteristic of this console…
  * [Background](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-3-1-background)
  * [Map](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-3-2-map)
  * [Displayed](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-3-3-displayed)

[![Image](https://www.copetti.org/images/consoles/snes/mode7/layer.325674b520bf46193209f90bb83a325c2c54e3079bb5e9f3a98e047cf889be09.png)](https://www.copetti.org/images/consoles/snes/mode7/layer.325674b520bf46193209f90bb83a325c2c54e3079bb5e9f3a98e047cf889be09.png)Rendered Background layer.[![Image](https://www.copetti.org/images/consoles/snes/mode7/map.c00ef0b232d03cd15e4d44204c1a20bcf0a42d86da370a1fb0226cd2ff66dd7d.png)](https://www.copetti.org/images/consoles/snes/mode7/map.c00ef0b232d03cd15e4d44204c1a20bcf0a42d86da370a1fb0226cd2ff66dd7d.png)Allocated Background map.[![Image](https://www.copetti.org/images/consoles/snes/mode7/displayed.a9416d191def1920c47a5d7a25f17011433d49ef8cac9193a129440526d4af58.png)](https://www.copetti.org/images/consoles/snes/mode7/displayed.a9416d191def1920c47a5d7a25f17011433d49ef8cac9193a129440526d4af58.png)Rendered frame on the screen.  
The first quarter of scan-lines uses another mode to simulate distance, Mode 7 starts at the second quarter (this is possible thanks to HDMA).Deconstruction of F-Zero (1990).
Introducing **Mode 7** , _yet another_ background mode - but this time, with a completely different way of working. While it can only render a single 8 bpp background layer, it provides the exclusive ability to apply the following **affine transformations** on that plane [[19]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-rgme):
  * Translation.
  * Scaling.
  * Rotation.
  * Reflection.
  * Shearing.


Mode 7 is controlled via a **rotation matrix** , which alters its parameters. Without delving into linear algebra, depending on the desired effect, the CPU must perform some trigonometric functions (sine and cosine) to populate the entries of this table accordingly. This is computationally expensive for the 65C816, even when using fixed-point precision. For this reason, with the 5A22, Ricoh integrated multiplication and division registers to offload some cycles.
By the way, you may notice that the list of transformations does not mention **perspective** , despite its presence in the example game, F-Zero. This effect is achieved by adjusting the rotation matrix at each HDMA call, creating a pseudo-3D effect in the process. This should give you an idea of just how versatile the S-PPU truly is!
Finally, due to the use of affine transformations, it is no longer useful to fetch adjacent pixels from VRAM. So, to maintain acceptable bandwidth, the memory map is restructured in a way that benefits the new pipeline. Thus, the first VRAM chip stores the **Tilemap** (where tiles are referenced), while the second stores the **Tileset** (where tiles are stored). Considering entries in both tables are 8 bits long, this setup allows the PPU 1 to retrieve references and tiles in a single cycle.
#### Generous circuits
Since Mode 7 requires additional computations, the PPU 1 incorporates dedicated circuitry to process the rotation matrix. Now, here is the interesting part: **it also exposes the registers for developers to access** when idle (in other words, when using Mode 0 to 6, or during V-Blank) [[20]](https://www.copetti.org/writings/consoles/super-nintendo#bib:cpu-multiplication).
The PPU 1’s multiplier is both faster and more capable than the CPU’s, as it accepts 16-bit numbers, both positive and negative (signed).
Reflecting on this 30 years later, I must say this concept is an earlier precursor to [computer shaders](https://www.copetti.org/writings/consoles/xbox-360/#the-impact-on-the-industry).
### More colour magic
Behind every rich frame is a flexible rendering pipeline. Well, if all the previous advancements weren’t impressive enough, the S-PPU features a **versatile colour blender** that enables to customise how layers are merged. Unlike other sprite engines with fixed rendering steps, Nintendo’s engineers exposed multiple parameters within the S-PPU’s pipeline, enabling developers to alter how certain pixels of different layers interact to form the final frame.
This functionality is collectively known as **Color Math** [[21]](https://www.copetti.org/writings/consoles/super-nintendo#bib:graphics-color_math), but it is also called ‘Screen Addition/Subtraction’ - despite also supporting division by two. In any case, this pave the way for **realistic transparency, dynamic lighting, and other creative effects**.
[![Image](https://www.copetti.org/images/consoles/snes/color_math/dk1.01dbbcacb19dfe4d08113a759ef957db82bfd79a96ec20f07065869509f96520.png)](https://www.copetti.org/images/consoles/snes/color_math/dk1.01dbbcacb19dfe4d08113a759ef957db82bfd79a96ec20f07065869509f96520.png)The lamp sways along with the light, such daunting effect is accomplished by altering the S-PPU’s masking options.[![Image](https://www.copetti.org/images/consoles/snes/color_math/dk2.3907aff602bd53b938d2e86c83e769c829ecb19b3b19300220b16cdc7ddd6964.png)](https://www.copetti.org/images/consoles/snes/color_math/dk2.3907aff602bd53b938d2e86c83e769c829ecb19b3b19300220b16cdc7ddd6964.png)The parrot follows you around with a torchlight, which can point to either direction and bounce. This plays very well with the overall atmosphere.Donkey Kong Country (1994) exploited the capabilities of the S-PPU’s blender to astonishing levels.
In essence, the process works as follows [[22]](https://www.copetti.org/writings/consoles/super-nintendo#bib:graphics-rgme_color_math):
  1. Internally, the S-PPU houses two rendering pipelines: **Main Screen** and **Sub Screen** , where programmers can assign backgrounds layers and the sprite layer to each.
     * The Sub Screen can also be filled with a solid colour instead of receiving layers.
     * High-resolution modes (Mode 5 and 6) consume the Sub Screen’s resources, preventing Color Math from working in those modes.
  2. The pixels of both screens can be masked using individual window parameters.
  3. The S-PPU separately merges the background layers within Main and Sub Screen, respecting the priority of each layer and window settings.
  4. Finally, the S-PPU lets programmers decide how to merge the content of Main Screen and Sub Screen. It can **add** or **subtract** the two screens, and then **divide** the result by two (achieving transparency effects).
     * Division by two is computationally cheap in digital circuits, as it only requires to shift the value one position to the right.


In the second _Donkey Kong Country_ example, Main Screen consists of a single white layer, while Sub Screen contains the rest of the scenery. However, the latter is encoded with **inverted colours**. At the last stage of the pipeline, the S-PPU applies subtraction and division, producing a correctly coloured frame with transparency effects and enhanced brightness - effectively simulating the torchlight.
### Cause of frame drops
On a different topic - what causes games to lag? When the V-Blank interrupt is triggered to allow graphics updates, the game may still be executing heavy code, causing it to miss the V-Blank window. As a result, graphics cannot be updated until the next V-Blank call, and since the frame remains unchanged, this manifests as a drop in frame-rate [[23]](https://www.copetti.org/writings/consoles/super-nintendo#bib:graphics-rgme_lag).
Conversely, extensive processing during a V-Blank can block the S-PPU from outputting the video signal, as the bus remains occupied. This can lead to black lines appearing during a scan, though this effect is barely noticeable since the frames refresh 50 or 60 times per second.
### A convenient video out
All of the aforementioned advancements would be meaningless unless the console could transmit its picture to the TV through a medium both can understand. With the Super Nintendo, the company debuted some sort of _universal-but-proprietary_ connection called **Multi Out** , capable of carrying many types of signals at the same time, including **Composite** , **S-Video** and **RGB** [[24]](https://www.copetti.org/writings/consoles/super-nintendo#bib:graphics-pinouts).
Nintendo bundled a ‘Multi Out-to-Composite’ cable with the console, as composite video was pretty much the common denominator of TVs at the time.
In Europe, however, the **SCART** port was widely popular, particularly among set-top boxes and VCRs. A major advantage of SCART is its ability to support multiple signal types, allowing AV equipment to select the most optimal format without compatibility issues. As far as I know, only French consumers were offered an official SCART cable that took advantage of the RGB pins exposed on the Super Nintendo [[25]](https://www.copetti.org/writings/consoles/super-nintendo#bib:graphics-manuel).
Consequently, Nintendo altered the pinout of its PAL consoles to comply with the SCART protocol, replacing the ‘composite sync’ pin with a 12-volt signal - which instructs the TV to use a 4:3 aspect ratio. Thus, while Multi Out is theoretically universal, RGB cables, if any, are region-specific.
I think the practical benefits of Multi Out have become more apparent in recent years, as it allows users to leverage the RGB output on their modern tellies without tampering with the console’s internals. However, unlike Composite and S-Video, RGB requires an extra ‘sync’ signal. For this, cables can be wired up to capture the sync signal from Composite or S-Video - or for best results, use a dedicated sync line called ‘composite sync’. Unfortunately, as noted earlier, the latter signal is exclusive to NTSC consoles.
* * *
## Audio
Just like its graphical abilities, the audio department of this console has undergone a significant overhaul. I would argue it even offers the most advanced synthesising techniques of its generation.
### Architecture
Some companies [partnered with Yamaha](https://www.copetti.org/writings/consoles/mega-drive-genesis/#audio), while others devised an [in-house solution](https://www.copetti.org/writings/consoles/pc-engine/#audio). Well, Nintendo partnered with **Sony** - the electronics conglomerate behind the _Walkman_ - to supply a sophisticated synthesiser.
And so, Sony delivered quite an audio subsystem, consisting of the following components:
  * **The S-DSP** : Plays **ADPCM samples** across **eight channels** , they are mixed and sent through the audio output. The S-DSP processes samples with **16-bit resolution** at a **32 kHz** sampling rate, and offers various sound manipulation techniques:
    * **Stereo Panning** : Distributes audio channels to create a stereo soundscape.
    * **ADSR Envelope Control** : Adjusts how the volume changes over time.
    * **Delay** : Simulates echo effects. It also includes a frequency filter to cut out selected frequencies during the feedback (not to be confused with _Reverb_!).
    * **Noise generator** : Generates pseudo-random waveforms resembling white static.
    * **Pitch modulation** : Allows some channels to influence each other’s pitch, similar to FM synthesis (used by [its competitor](https://www.copetti.org/writings/consoles/mega-drive-genesis/#audio)).
  * **The SPC700 CPU** (also known as ‘S-SMP’): An independent 8-bit CPU that drives the S-DSP and receives commands from the main CPU [[26]](https://www.copetti.org/writings/consoles/super-nintendo#bib:audio-smp).
  * **64 KB of PSRAM** : Stores audio data and programs, with the main CPU responsible for loading content into it.
    * If ‘Delay’ is enabled, some memory is reserved for feedback data. This is can be dangerous - if not managed carefully, feedback storage could override existing data!


The audio subsystem operates in parallel with the main CPU. When the console powers on, the SPC700 boots a 64-byte internal ROM that sets it up to receive commands from the main CPU [[27]](https://www.copetti.org/writings/consoles/super-nintendo#bib:audio-spc). After this setup, it remains idle until instructed.
  * [Melody](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-4-1-melody)
  * [Drums](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-4-2-drums)
  * [Complete](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-4-3-complete)

No support for video.Channels used for melody. No support for video.Drums are discriminated for demonstration purposes. No support for video.All audio channels.Oscilloscope display of Star Fox (1993).
For the S-SMP to do independent work, it needs to load a type of program known as **Sound Driver**. This software instructs the chip on how to manipulate raw audio data sent by the main CPU to PSRAM, as well as how to control the S-DSP.
As evident, the sound subsystem was a major leap forward compared to previous generations, but it also posed significant programming challenges. The documentation provided by Nintendo was infamous for its vague explanations and omission of critical features, forcing developers to conduct their own research.
As a result, a wide variety of sound drivers emerged in the market [[28]](https://www.copetti.org/writings/consoles/super-nintendo#bib:audio-drivers), with some uncovering impressive capabilities.
### Pitch control
Pitch bending enables to produce distinct notes using the same sample. Well, the S-SMP included a useful bender to alter the pitch in a smooth manner. Take a look at this extracted channel from Mother 2/Earthbound @[fig-pitch_bend], both examples come from the original soundtrack, however, the first one has the pitch control disabled.
No support for video.No pitch bend. No support for video.With pitch bend enabled.Oscilloscope display of Mother 2/Earthbound (1994).
### Evolution from the NES
To visualise the evolution of sound from the NES to the Super Nintendo, here is an excerpt from two music scores - one from an NES game and another from its Super Nintendo sequel. Both feature the same composition.
No support for video.Mother (1989). No support for video.Mother 2/Earthbound (1994).Oscilloscope display of the same score across the two different games.
### Advanced usage
  * [Melody](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-5-1-melody)
  * [Drums](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-5-2-drums)
  * [Complete](https://www.copetti.org/writings/consoles/super-nintendo#nestedtab-5-3-complete)

No support for video.Channels used for melody. No support for video.Channels used for drums. No support for video.All audio channels.Oscilloscope display during a game of Kirby’s Dream Land 3 (1997).
Here’s a more instrument-rich composition that takes great advantage of pitch bending, echo and envelope.
This combination of techniques allowed the music to only require five channels in total, leaving the other three for sound effects.
### Stereo confusion
The S-DSP’s volume controls are organised into signed 8-bits values [[29]](https://www.copetti.org/writings/consoles/super-nintendo#bib:audio-gst), meaning that volume levels can be set to **negative values**. _But hang on_ , if ‘0’ represents mute, what happens when the volume is set to ‘-1’? Well, it **inverts the signal**.
This technique is particularly useful for creating a **surround effect** , accomplished by setting the stereo channels **out of phase** - where one channel outputs the normal signal while the other outputs the same signal but inverted.
Unfortunately, abusing this feature results in very unpleasant results, such as the feeling that the music is playing inside your head. For this reason, most SNES emulators bypass this setting altogether.
Additionally, out-of-phase stereo is cancelled out on mono devices, so those games needed to provide a stereo/mono selector to avoid muting their own soundtrack.
* * *
## Games
To be blunt, the main program is written in plain **65816 assembly** and the music driver is written in **SPC700 assembly**. Needless to say, you won’t find any of the commodities available on 21st-century equipment.
There were, however, some tools distributed by Nintendo, Intelligent Systems and Ricoh to make life easier for programmers, these included [[30]](https://www.copetti.org/writings/consoles/super-nintendo#bib:games-sdk):
  * Different types of **development units** , capable of being controlled by a **debugger** from a host machine (typically running MS-DOS).
  * **Flashable cartridges** (a.k.a. _Flashcarts_) - not for _piracy_ , but to enable developers test their code on retail units.
  * 65816 and SPC700 **assemblers**.
  * **Development Manuals** explaining from a low-level perspective how this console works. These often included guidelines and norms that developers had to follow to get their game approved by Nintendo (necessary for distribution).


Curiously enough, several game studios - including Argonaut Software, Accolade, and SN Systems - developed custom in-house equipment, often providing more capabilities than the official offerings (e.g. memory editors, floppy disk readers, ISA-based devkits, etc.) [[31]](https://www.copetti.org/writings/consoles/super-nintendo#bib:games-devkit).
### Cartridge configuration
When it comes to accessing the cartridge, things get a lot more confusing compared to the relatively simpler mapping model of the NES. I find it interesting nonetheless, especially for understanding how it could be expanded.
The 65C816 features a 24-bit address bus, enabling to access up to 16 MB worth of data. However, due to the console’s architecture, a portion of the address space is reserved for [memory-mapped components](https://www.copetti.org/writings/consoles/nes/#memory). Moreover, the 65C816 only comes with 16 address lines, which are then combined with internal registers to construct a 24-bit address. This is analogous to housing an [internal mapper](https://www.copetti.org/writings/consoles/pc-engine/#memory-access) and requiring [bank switching](https://www.copetti.org/writings/consoles/nes/#cartridgegame-data) to access extra data beyond the boundaries of the address bus. If you explore other systems of the same generation, you’ll find this methodology somewhat familiar.
[![Image](https://www.copetti.org/images/consoles/snes/cartridges.ed8ff989d1d7b8e521eab62ce18408dfcca9a103be7ca1c659b6fe2d0425a6b1.png)](https://www.copetti.org/images/consoles/snes/cartridges.ed8ff989d1d7b8e521eab62ce18408dfcca9a103be7ca1c659b6fe2d0425a6b1.png)Example cartridge boards designed with different configurations [[32]](https://www.copetti.org/writings/consoles/super-nintendo#bib:photography-amos).  
From top to bottom: LoROM (dual ROM with battery-backed SRAM), LoROM (single ROM with battery-backed SRAM) and LoROM (single ROM)
That being said, when it comes to designing a cartridge, there are many ways to electrically connect the address pins between the ROM and CPU, each utilising bank switching in a different way.
There are two fundamental models that enables accessing up to **4 MB of ROM** and **64 KB of SRAM** [[33]](https://www.copetti.org/writings/consoles/super-nintendo#bib:games-memory), and they work as follows:
  * With the **LoROM Model** , ROM Data is arranged in 32 KB chunks with 128 banks available to choose from [[34]](https://www.copetti.org/writings/consoles/super-nintendo#bib:games-bazzinotti). SRAM, though fitting within two banks, is accessible across 15 banks, where ROM data is also present.
    * This setup requires frequent bank switching during execution. On the other side, half of the banks are also mapped to WRAM, meaning ROM, SRAM, and WRAM can be accessed without switching banks.
  * With the **HiROM Model** , ROM space is structured into full banks, meaning data is stored in 64 KB chunks across 64 banks. This configuration reduces the need for bank switching, but at the cost of not being able to read ROM, WRAM and SRAM within the same bank.


In both cases, a significant portion of ROM space is mirrored across the leftover area of the CPU’s address space. However, here’s the interesting part: one half of the space operates at ~2.68 MHz while the other can reach **3.58 MHz** - but only if the ROM chip supports the higher speed and the CPU’s `FastROM` flag is enabled [[35]](https://www.copetti.org/writings/consoles/super-nintendo#bib:games-registers).
Additionally, cartridges that bundle SRAM must house a **MAD-1** (or similar) chip, which performs address decoding. This component is particularly crucial for correctly latching the pins that select between ROM and SRAM chips [[36]](https://www.copetti.org/writings/consoles/super-nintendo#bib:games-pcb).
#### Beyond convention
Now, when programmers require more space, derivative models of LoROM and HiROM come into place. Two common variations, known as **ExHiROM** and **ExLoROM** , extend the ROM’s addressing space by reducing the mirrored area. Both can access **~7.9 MB of ROM**.
[![Image](https://www.copetti.org/images/consoles/snes/fox.b6ee76ab3f91235cadb35b8920875c22d420ee601184639eee35b51d98bb43b2.png)](https://www.copetti.org/images/consoles/snes/fox.b6ee76ab3f91235cadb35b8920875c22d420ee601184639eee35b51d98bb43b2.png)Star Fox (1993) uses the Super FX GSU chip to render 3D surfaces. Behind the scenes, the S-PPU only sees a background layer made of _erratic_ tiles.
Alternatively, and most importantly, LoRom and HiROM can also be adapted to accommodate **enhancement chips** within the cartridge. These are additional processors that expand the capabilities of the console. To name a few examples of new configurations:
  * The **MMC** model enables bank switching via the local enhancement chip. This was used by components like the **S-DD1** or the **SPC7110** , both function as hardware tile decompressors.
  * The **Super Accelerator System** model was designed for the highly regarded **SA-1** , a secondary **65C816-based CPU** operating at **10.74 MHz** with extra functionality. It builds upon the MMC model, incorporating new circuitry for the additional memory-mapped components.
  * Two extra configurations - one based on LoROM and the other on HiROM - make way for the **DSP series**. These chips are derivatives of the NEC µPD77C25 CPU, but running a different program. They provide vector and matrix computations [[37]](https://www.copetti.org/writings/consoles/super-nintendo#bib:games-dsp). Various games have used them for affine transformations, graphics decompressing and shortest path calculations.
  * The **SFX** model targets the popular **Super FX GSU** chip. This configuration maps up to 8 MB of ROM, with 2 MB shared between the main CPU and the Super FX. The rest of the address space includes additional backup RAM and SRAM. Developed by Argonaut, the Super FX is a proprietary processor specialising in **3D surface rendering** and **2D affine transformations**. The processed graphics are then streamed as tiles for the S-PPU to display. Several notable games leveraged this technology to render 3D models and extend Mode 7 for sprites (as Mode 7 can only transform backgrounds).


It’s difficult to overlook the impact this engineering had on 90s gaming, with many titles surpassing the console’s expectations - and without requiring expansion modules and whatnot. You could say this complicated Nintendo’s plans for a successor console, which may explain the cancellation of advanced games like Star Fox 2.
* * *
## Anti-piracy / Region Lock
With the Super Nintendo, Nintendo assumed again the sole authority over game distribution. To enforce its policies, the company devised three layers of protection to prevent unauthorised cartridge distribution and circumvention of royalties.
Firstly, the external shape of cartridges **is different between regions** , so they won’t fit on consoles from different areas. Be as it may, this could be easily bypassed using a third-party adapter.
Secondly, like the NES, this console still incorporates the [10NES protection system](https://www.copetti.org/writings/consoles/nes/#anti-piracy-and-region-lock) to lock out unauthorised distributors. However, the CIC chip was eventually cloned.
As a final layer - specifically designed to combat bootlegging - games included a chain of piracy checks within their program, such as:
  1. **SRAM size verifications** : Bootleg cartridges often contain large SRAM blocks to accommodate various games.
  2. **Code integrity checks** : A series of checksums embedded throughout the game’s code verify whether the previous SRAM size verification routines have been removed. These checks are dispersed at different stages of the game, making them difficult to locate and remove.


While these measures could be nullified by manually stripping out the routines, this was a time-consuming task. After all, they would be scattered around the game only to upset the player (and eventually make them buy a legitimate copy). Truth to be told, you’ll notice that most ROMs available online have had all their piracy checks removed.
* * *
## That’s all folks
[![Image](https://www.copetti.org/images/consoles/snes/mysnes.07dae864d5731f4ed0cb333f0558c486e5516f4ef861ccc4b75b20da6c777552.png)](https://www.copetti.org/images/consoles/snes/mysnes.07dae864d5731f4ed0cb333f0558c486e5516f4ef861ccc4b75b20da6c777552.png)My modded SNES with an American cartridge.  
That game was only released in the states. Luckily, a lad was selling it in Glasgow!
* * *
## Contributing
This article is part of the [Architecture of Consoles](https://www.copetti.org/writings/consoles/) series. If you found it interesting then please consider donating. Your contribution will be used to fund the purchase of tools and resources that will help me to improve the quality of existing articles and upcoming ones.
[![Donate with PayPal](https://www.copetti.org/images/paypal_donate.png)](https://www.paypal.com/donate/?hosted_button_id=3GXQA6XPL7G3S)
[![Become a Patreon](https://www.copetti.org/images/patreon.png)](https://www.patreon.com/copetti)
You can also buy the [book editions](https://www.copetti.org/writings/consoles/materials/book/) in English. I treat profits as donations.
[![eBook edition](https://www.copetti.org/images/consoles/books/ebooks_banner.0d180c0136e4c9345bc0ab4f7a0224849a292326d2679d610ea945054383a996.jpg)](https://www.copetti.org/writings/consoles/materials/book/)
A list of desirable tools and latest acquisitions for this article are tracked in here:
```
### Interesting hardware to get (ordered by priority)
- Any cartridge using enhancement chips (£5 - ?)
### Acquired tools used
- PAL SNES modded to play 60Hz NTSC (£40)
- NTSC game (not cheap...)
```

Alternatively, you can help out by [suggesting changes](https://github.com/flipacholas/Architecture-of-consoles) and/or [adding translations](https://github.com/flipacholas/Architecture-of-consoles).
* * *
## Copyright and permissions
This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). You may use it for your work at no cost, even for commercial purposes. But you have to respect the license and reference the article properly. Please take a look at the following guidelines and permissions:
Article information and referencing
For any referencing style, you can use the following information:
  * **Title of article** : Super Nintendo / Famicom Architecture - A Practical Analysis
  * **Author** : Rodrigo Copetti
  * **URL** : <https://www.copetti.org/writings/consoles/super-nintendo/>
  * **Date of publication** : June 28, 2019
  * **Last modified** : June 14, 2025


For instance, to use with BibTeX:
```
@misc{copetti-snes,
    url = {https://www.copetti.org/writings/consoles/super-nintendo/},
    title = {Super Nintendo / Famicom Architecture - A Practical Analysis},
    author = {Rodrigo Copetti},
    year = {2019}
}

```

or a IEEE style citation:
```
[1]R. Copetti, "Super Nintendo / Famicom Architecture - A Practical Analysis", Copetti.org, 2019. [Online]. Available: https://www.copetti.org/writings/consoles/super-nintendo/. [Accessed: day- month- year].

```

Special use in multimedia (Youtube, Twitch, etc)
I only ask that you at least state the author’s name, the title of the article and the URL of the article, using any style of choice.
You don’t have to include all the information in the same place if it’s not feasible. For instance, if you use the article’s imagery in a Youtube video, you may state either the author’s name or URL of the article at the bottom of the image, and then include the complete reference in the video description. In other words, for any resource used from this website, let your viewers know where it originates from.
[This is a very nice example](https://www.twitch.tv/videos/1187360494?t=00h25m55s) because the channel shows this website directly and their viewers know where to find it. In fact, I was so impressed with their content and commentary that [I gave them an interview](https://www.twitch.tv/kenobisboch/video/1226597304) 🙂.
Appreciated additions
If this article has significantly contributed to your work, I would appreciate it if you could dedicate an acknowledgement section, just like I do with the people and communities that helped me.
This is of course optional and beyond the requirements of the CC license, but I think it’s a nice detail that makes us, the random authors on the net, feel part of something bigger.
Third-party publishing
If you are interested in publishing this article on a third-party website, please get in touch.
If you have translated an article and wish to publish it on a third-party website, I tend to be open about it, but please contact me first.
* * *
## Sources / Keep Reading
### Audio
  * vgmpf.com, [S-SMP](http://www.vgmpf.com/Wiki/index.php?title=S-SMP). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:26)
  * Snarius, [Super NES programming/SPC700 reference](https://en.wikibooks.org/wiki/Super_NES_Programming/SPC700_reference). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:27)
  * Game Developer Research Institute, [Super famicom/super NES sound driver list](http://gdri.smspower.org/wiki/index.php/Super_Famicom/Super_NES_Sound_Driver_List). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:28)
  * GST Channel, [The sound capabilities of the SNES](https://www.youtube.com/watch?v=dtK0t8k6akg) (Interesting compilation of audio capabilities). Youtube. [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:29)


### CPU
  * Nintendo of America, [SNES development manual](https://archive.org/details/SNESDevManual). 1993. [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:11)
  * Brian Benchoff, [Winning the console wars – an in-depth architectural study](https://hackaday.com/2015/11/06/winning-the-console-wars-an-in-depth-architectural-study/).
  * Retro Game Mechanics Explained (Alex "Dotsarecool" Losego), [Super NES features](https://www.youtube.com/playlist?list=PLHQ0utQyFw5KCcj1ljIhExH_lvGwfn6GV). Youtube. [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:19)
  * Snarius, [Super NES programming/SNES specs](https://en.wikibooks.org/wiki/Super_NES_Programming/SNES_Specs).
  * Snarius, [Super NES programming/DMA tutorial](https://en.wikibooks.org/wiki/Super_NES_Programming/DMA_tutorial). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:18)
  * ChibiAkumas, [Learn multi platform 65816 assembly programming... For ultimate power!](https://www.chibiakumas.com/65816/). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:5)
  * Super Nintendo Development Wiki, [65816 reference](https://wiki.superfamicom.org/65816-reference). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:3)
  * Bruce Clark, [65C816 opcodes](http://www.6502.org/tutorials/65c816opcodes.html). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:4)
  * wiki.nesdev.com, [CPU (6502 unofficial opcodes)](https://wiki.nesdev.com/w/index.php/CPU_unofficial_opcodes). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:2)
  * Computer History Museum, [Oral history of william david “bill” mensch, jr.](https://archive.computerhistory.org/resources/access/text/2015/06/102739969-05-01-acc.pdf). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:1)
  * Nesdev users, [65816/SNES open bus/MDR mystery, (re: The latest RGMEx video)](https://forums.nesdev.org/viewtopic.php?t=24536) (accessed 22-April-2025). Nesdev Forums. [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:10)
  * SNESdev Wiki contributors, [Multiplication](https://snes.nesdev.org/wiki/Multiplication) (accessed 16-May-2025). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:20)
  * SNESdev Wiki contributors, [Division](https://snes.nesdev.org/wiki/Division) (accessed 16-May-2025). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:7)


### Games
  * caitsith2.com, [SNES cartridge and chips pinouts](https://www.caitsith2.com/snes/flashcart/cart-chip-pinouts.html).
  * snescentral.com, [SNES PCB list](https://snescentral.com/pcblisting.php). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:36)
  * Michael Bazzinotti, [SNES LoRom memory model](https://web.archive.org/web/20190311181601/https://www.cs.umb.edu/~bazz/snes/cartridges/lorom.html). Archived. [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:34)
  * Retro Reversing, [SNES (super famicom) development kit hardware](https://www.retroreversing.com/super-famicom-snes-development-kit/). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:31)
  * Retro Reversing, [SNES (super famicom) software development kit (SDK)](https://www.retroreversing.com/super-famicom-snes-sdk/). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:30)
  * Super Nintendo Development Wiki, [Registers](https://wiki.superfamicom.org/registers). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:35)
  * Wikibooks, [Super NES programming/SNES memory map](https://en.wikibooks.org/w/index.php?title=Super_NES_Programming/SNES_memory_map&oldid=4072115) (\\[Online; accessed 18-November-2022\\]). 2022. [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:33)
  * Snes9x DSP Team, [DSP1 gamepaks](https://web.archive.org/web/20110610122211/http://users.tpg.com.au/advlink/dsp/dsp1.html). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:37)
  * Bucket Mouse, [The SNES cartridge, briefly explained](https://mousebitelabs.com/2019/05/18/custom-pcb-explanation/). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:36)


### Graphics
  * Alyssa Keil, [Super nintendo graphics guide](https://megacatstudios.com/blogs/press/super-nintendo-graphic-guide). 2017. [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:12)
  * Alyssa Keil, [SNES sprite engine design guidelines](https://megacatstudios.com/blogs/press/snes-sprite-engine-design-guidelines). 2018. [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:17)
  * David Piepgrass, [Qwertie’s SNES documentation plus DMA revision 6 - 2.1, non-profit use only](https://media.smwcentral.net/Ersanio/SMWCstuff/Advanced%20documentation/qsnesdoc.html). 1998. [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:9)
  * Nintendo, [Super nintendo - manuel d’instructions (france)](http://www.ffviman.fr/switch-snes/notice-eur-p-iii-iv.html). 1992. [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:25)
  * pinouts.ru, [Nintendo SNES pinouts](https://pinouts.ru/dev/Nintendo/SNES/). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:24)
  * Jademalo, [4:3 -> 8:7 aspect ratio correction for SNES](https://videogameperfection.com/forums/topic/43-87-aspect-ratio-correction-for-snes/). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:13)
  * Fabien Sanglard, [Designing the super nintendo video system](https://fabiensanglard.net/snes_video/). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:14)
  * SNESdev Wiki contributors, [Color math](https://snes.nesdev.org/wiki/Color_math) (accessed 17-May-2025). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:21)
  * Retro Game Mechanics Explained (Alex "Dotsarecool" Losego), [Color math - super nintendo entertainment system features pt. 03b](https://www.youtube.com/watch?v=zcoU6-9_fDM). Youtube. [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:22)
  * Retro Game Mechanics Explained (Alex "Dotsarecool" Losego), [Lag & blanking - super nintendo entertainment system features pt. 06](https://www.youtube.com/watch?v=Q8ph2OVqZeM). Youtube. [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:23)
  * Fabien Sanglard, [How the SNES graphics system works](https://fabiensanglard.net/snes_ppus_how/). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:15)


### Photography
  * Yaca2671, [Motherboard](https://commons.wikimedia.org/wiki/File:SNES-CPU-RGB01_01.jpg).
  * Evan Amos, [The vanamo online game museum](https://commons.wikimedia.org/wiki/User:Evan-Amos). [↩︎](https://www.copetti.org/writings/consoles/super-nintendo#bibref:32)
  * Rodrigo Copetti (Me), [Diagrams, casual photos and game screenshots](https://www.copetti.org/).


* * *
## Changelog
It’s always nice to keep a record of changes. For a complete report, you can check the [commit log](https://github.com/flipacholas/Architecture-of-consoles/commits/master/articles/super-nintendo.Rmd.md). Alternatively, here’s a simplified list:
```
### 2025-05-18
- Overall improvements to prepare for a book release.
- Extended arithmetic information.
- Added Colour Math section, thanks Jellema for the pointers.
### 2024-09-30
- Added photos taken using Christopher Rivett's collection.
### 2024-01-14
- Added paragraphs about WRAM.
- Added mention of the official French SCART cable, thanks Hugues.
### 2022-11-19
Super revamp:
- Expanded CPU section with more information and history
- Added more information about graphics effects and anomalies.
- Improved the other sections with lots of more information.
### 2021-07-10
- Extended Mode-7 paragraph
### 2020-09-23
- Added info about video out
### 2020-08-23
- Added more CPU info, thanks @J-P
### 2019-12-08
- Expanded the Audio section.
### 2019-10-28
- Some corrections and improvements.
### 2019-09-17
- Added a quick introduction
### 2019-09-01
- Added my SNES 🧐
### 2019-08-29
- Better wording
### 2019-06-28
- Ready for publication
```

* * *
[« Neo Geo Architecture](https://www.copetti.org/writings/consoles/neogeo/) [Sega Saturn Architecture »](https://www.copetti.org/writings/consoles/sega-saturn/)
![Rodrigo Copetti](https://www.copetti.org/favicon/favicon.png)
### Rodrigo Copetti
I hope you have enjoyed this article! If you want to know more about the author [tap here](https://www.copetti.org/about/) and if you would like to support him [tap here](https://www.copetti.org/support/) instead
[Tweet ](https://twitter.com/intent/tweet?text=Super%20Nintendo%20%2f%20Famicom%20Architecture%20%7c%20A%20Practical%20Analysis%20https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fsuper-nintendo%2f)[Share ](javascript:void\(0\))[Share ](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fsuper-nintendo%2f&title=Super%20Nintendo%20%2f%20Famicom%20Architecture%20%7c%20A%20Practical%20Analysis&summary=An%20in-depth%20analysis%20that%20explains%20how%20this%20console%20works%20internally&source=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fsuper-nintendo%2f)[Share](https://reddit.com/submit?url=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fsuper-nintendo%2f&title=Super%20Nintendo%20%2f%20Famicom%20Architecture%20%7c%20A%20Practical%20Analysis)
[Switch to classic edition](https://classic.copetti.org/writings/consoles/super-nintendo/)
Rodrigo Copetti © 2025 [](https://www.copetti.org/index.xml)
[About the website and its content](https://www.copetti.org/disclaimer/)
rsslinkedintwitterblueskygithub facebookreddit
