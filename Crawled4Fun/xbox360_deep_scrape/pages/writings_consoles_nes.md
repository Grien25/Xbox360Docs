# NES / Famicom Architecture | A Practical Analysis

**Source:** https://www.copetti.org/writings/consoles/nes

[Home](https://www.copetti.org/)
[Consoles](https://www.copetti.org/writings/consoles/)
[About](https://www.copetti.org/about/)
[Support](https://www.copetti.org/support/)
# NES / Famicom Architecture
## A practical analysis by Rodrigo Copetti
[](https://github.com/flipacholas/Architecture-of-consoles)[](https://crowdin.com/project/architecture-of-consoles)[](https://www.copetti.org/writings/consoles/materials/readings/)[](https://www.copetti.org/writings/consoles/nes)
If you use accessibility tools or old browsers, [switch to the ‘classic’ edition](https://classic.copetti.org/writings/consoles/nes/).
🇬🇧 - English 🇪🇸 - Español 🇧🇷 - Português (Brasil) 🇹🇷 - Türkçe 🇦🇪 - اَلْعَرَبِيَّةُ 🇨🇳 - 简体字 🇰🇷 - 한국어 👋 - Add translation
* * *
Book edition
[![eBook edition](https://www.copetti.org/images/consoles/_covers/en/nes_hu_579b41493f5a83a6.jpg)](https://www.copetti.org/writings/consoles/materials/book/)
This article is also published in many bookstores for the benefit of offline readers. The eBooks are DRM-free, while the printed editions compile multiple articles and feature original photography at full resolution.
You can find printed compilations [here](https://www.amazon.com/dp/B0F4P5RB25?binding=paperback), and individual eBooks at [Amazon Kindle](https://www.amazon.com/dp/B0B5VM3NHS), [Apple Books](https://books.apple.com/us/author/rodrigo-copetti/id1632545359?see-all=books), [Kobo](https://www.kobo.com/us/en/search?query=Architecture+of+Consoles%3a+A+Practical+Analysis&fcsearchfield=Series&seriesId=7e46f843-4aee-53b4-97c2-82782e951af5) and [other stores](https://www.copetti.org/writings/consoles/materials/book/). The proceeds support the improvement of current articles and the development of new ones.
For more information, please take a look at [here](https://www.copetti.org/writings/consoles/materials/book/).
* * *
Table of Contents
  1. [Supporting imagery](https://www.copetti.org/writings/consoles/nes#imagery)
  2. [A quick introduction](https://www.copetti.org/writings/consoles/nes#a-quick-introduction)
  3. [Models and variants](https://www.copetti.org/writings/consoles/nes#models-and-variants)
  4. [CPU](https://www.copetti.org/writings/consoles/nes#cpu)
    1. [A bit of context](https://www.copetti.org/writings/consoles/nes#a-bit-of-context)
    2. [Core functionality](https://www.copetti.org/writings/consoles/nes#core-functionality)
      1. [Ricoh’s licensing enigma](https://www.copetti.org/writings/consoles/nes#ricohs-licensing-enigma)
      2. [Scrapped functions](https://www.copetti.org/writings/consoles/nes#scrapped-functions)
    3. [Memory](https://www.copetti.org/writings/consoles/nes#memory)
      1. [Segmentation Fault](https://www.copetti.org/writings/consoles/nes#segmentation-fault)
      2. [Cartridge/game data](https://www.copetti.org/writings/consoles/nes#cartridgegame-data)
      3. [Going beyond existing capabilities](https://www.copetti.org/writings/consoles/nes#going-beyond-existing-capabilities)
  5. [Graphics](https://www.copetti.org/writings/consoles/nes#graphics)
    1. [Organising the content](https://www.copetti.org/writings/consoles/nes#organising-the-content)
    2. [Constructing the frame](https://www.copetti.org/writings/consoles/nes#constructing-the-frame)
      1. [Tiles](https://www.copetti.org/writings/consoles/nes#tab-1-1-tiles)
      2. [Background Layer](https://www.copetti.org/writings/consoles/nes#tab-1-2-background-layer)
      3. [Sprite Layer](https://www.copetti.org/writings/consoles/nes#tab-1-3-sprite-layer)
      4. [Background Split](https://www.copetti.org/writings/consoles/nes#tab-1-4-background-split)
      5. [Result](https://www.copetti.org/writings/consoles/nes#tab-1-5-result)
    3. [Secrets and limitations](https://www.copetti.org/writings/consoles/nes#secrets-and-limitations)
      1. [Multi-Scrolling](https://www.copetti.org/writings/consoles/nes#tab-2-1-multi-scrolling)
      2. [Tile-Swapping](https://www.copetti.org/writings/consoles/nes#tab-2-2-tile-swapping)
      3. [Curious behaviour](https://www.copetti.org/writings/consoles/nes#tab-2-3-curious-behaviour)
  6. [Audio](https://www.copetti.org/writings/consoles/nes#audio)
    1. [Functionality](https://www.copetti.org/writings/consoles/nes#functionality)
      1. [Pulse](https://www.copetti.org/writings/consoles/nes#tab-3-1-pulse)
      2. [Triangle](https://www.copetti.org/writings/consoles/nes#tab-3-2-triangle)
      3. [Noise](https://www.copetti.org/writings/consoles/nes#tab-3-3-noise)
      4. [Sample](https://www.copetti.org/writings/consoles/nes#tab-3-4-sample)
    2. [Secrets and limitations](https://www.copetti.org/writings/consoles/nes#secrets-and-limitations-1)
      1. [Extra Channels](https://www.copetti.org/writings/consoles/nes#tab-4-1-extra-channels)
      2. [Tremolo](https://www.copetti.org/writings/consoles/nes#tab-4-2-tremolo)
    3. [A more refined observation](https://www.copetti.org/writings/consoles/nes#a-more-refined-observation)
      1. [Introduction to spectrograms](https://www.copetti.org/writings/consoles/nes#introduction-to-spectrograms)
      2. [Plotting the APU](https://www.copetti.org/writings/consoles/nes#plotting-the-apu)
        1. [Pulse](https://www.copetti.org/writings/consoles/nes#tab-5-1-pulse)
        2. [Triangle](https://www.copetti.org/writings/consoles/nes#tab-5-2-triangle)
        3. [Noise](https://www.copetti.org/writings/consoles/nes#tab-5-3-noise)
        4. [Sample](https://www.copetti.org/writings/consoles/nes#tab-5-4-sample)
        5. [Sawtooth](https://www.copetti.org/writings/consoles/nes#tab-5-5-sawtooth)
      3. [Conclusion](https://www.copetti.org/writings/consoles/nes#conclusion)
  7. [Games](https://www.copetti.org/writings/consoles/nes#games)
    1. [The alternative medium](https://www.copetti.org/writings/consoles/nes#the-alternative-medium)
  8. [Anti-piracy and region lock](https://www.copetti.org/writings/consoles/nes#anti-piracy-and-region-lock)
  9. [That’s all folks](https://www.copetti.org/writings/consoles/nes#thats-all-folks)
  10. [Copyright and permissions](https://www.copetti.org/writings/consoles/nes#referencing)
  11. [Sources / Keep Reading](https://www.copetti.org/writings/consoles/nes#sources)
  12. [Contributing](https://www.copetti.org/writings/consoles/nes#contributing)
  13. [Changelog](https://www.copetti.org/writings/consoles/nes#changelog)


* * *
## Supporting imagery
  * [Model](https://www.copetti.org/writings/consoles/nes#cover-model)
  * [Motherboard](https://www.copetti.org/writings/consoles/nes#cover-motherboard)
  * [Diagram](https://www.copetti.org/writings/consoles/nes#cover-diagram)


### Model
  * [International](https://www.copetti.org/writings/consoles/nes#cover-model-international)
  * [Japanese](https://www.copetti.org/writings/consoles/nes#cover-model-japanese)

[![International](https://www.copetti.org/images/consoles/nes/international.2260a04d73e81185a57694fffab4548ad5682f9db806f3620060487d455bef4d.png)](https://www.copetti.org/images/consoles/nes/international.2260a04d73e81185a57694fffab4548ad5682f9db806f3620060487d455bef4d.png)The Nintendo Entertainment System (NES).  
Released on 18/10/1985 in America and 01/09/1986 in Europe.[![Japanese](https://www.copetti.org/images/consoles/nes/japanese.f34aa402aa8708a07cb8dfdef8723ee5044529e343decc7d66f779e0f35b1c61.png)](https://www.copetti.org/images/consoles/nes/japanese.f34aa402aa8708a07cb8dfdef8723ee5044529e343decc7d66f779e0f35b1c61.png)The Famicom.  
Released on 15/07/1983 in Japan.
### Motherboard
  * [Original](https://www.copetti.org/writings/consoles/nes#cover-motherboard-original)
  * [Marked](https://www.copetti.org/writings/consoles/nes#cover-motherboard-marked)

[![Motherboard](https://www.copetti.org/images/consoles/nes/motherboard.9b1c6cda39500a1e464dc64dacc041f2f1956b3de5a833acc366da3bab2b7724.png)](https://www.copetti.org/images/consoles/nes/motherboard.9b1c6cda39500a1e464dc64dacc041f2f1956b3de5a833acc366da3bab2b7724.png)Motherboard  
Showing the 'NES' variant.[![Motherboard](https://www.copetti.org/images/consoles/nes/motherboard_marked.823b9c5f3ec657fabf5b86e6f6d8c1905ee7cf065b70cdebb4ce5e6e824eb774.png)](https://www.copetti.org/images/consoles/nes/motherboard_marked.823b9c5f3ec657fabf5b86e6f6d8c1905ee7cf065b70cdebb4ce5e6e824eb774.png)Motherboard with important parts labelled
### Diagram
[![Diagram](https://www.copetti.org/images/consoles/nes/_diagrams/main.fc816704bde99a30b84d0a9870f12ec3c5ccd15a23b00a72d8003e0ef43532b7.png)](https://www.copetti.org/images/consoles/nes/_diagrams/main.fc816704bde99a30b84d0a9870f12ec3c5ccd15a23b00a72d8003e0ef43532b7.png)Main architecture diagram
* * *
## A quick introduction
At first glance, the NES appears to be just another 6502 computer, with a sophisticated case and a controller.
And while this is _technically_ true, let me show you why the CPU is not the _central_ part of this system.
* * *
## Models and variants
[![Image](https://www.copetti.org/images/consoles/nes/betacord.2eb960d3bedfa00ab18da90456d2c4038768a0aa9ba7f4a101e49174a877eb8f_hu_d942e4d9c2c72a90.png)](https://www.copetti.org/images/consoles/nes/betacord.2eb960d3bedfa00ab18da90456d2c4038768a0aa9ba7f4a101e49174a877eb8f.webp)A typical Betamax recorder. This and similar appliances influenced the international design of the NES. I spotted this particular one at The Centre for Computing History (Cambridge, UK) when I visited in August 2024.
Nintendo ended up shipping lots of different variants of the same console across the world [[1]](https://www.copetti.org/writings/consoles/nes#bib:general-variants) and even though they all share the same architecture, many look dramatically different and some may include built-in accessories. So, to keep it simple for this article, I’ll focus on the two most popular revisions:
  * The **Family Computer** (known as _Famicom_) was the first incarnation, but was only released in Japan. This toy-looking design features two non-removable controllers (from which the second controller bundles an internal microphone), a front socket for the light gun (called _Zapper_), RF video out (using NTSC-J signal) and extra pins in the cartridge slot to expand the audio capabilities.
  * The **Nintendo Entertainment System** (known as _NES_) was the redesigned edition for western audiences living in North America, Europe and Oceania; with a look and mechanism that matches the common VHS/Betamax player. On the technical side, the controllers are now detachable (and microphone-lacking) and the video out has been improved with extra NTSC/PAL composite RCA connectors, although the audio expansion has been replaced with an anti-piracy subsystem. To top it off, the bottom of the case seals an ‘expansion port’ that was left unused, along with extra cartridge pins that communicate to that port [[2]](https://www.copetti.org/writings/consoles/nes#bib:general-cartridge).


Because the author grew up with the ‘NES’ name, I will default to using that term to refer to the console in general, but I will switch to ‘Famicom’ when referring to unique capabilities only found in the Japanese variant.
* * *
## CPU
The NES’s CPU is a **Ricoh 2A03** [[3]](https://www.copetti.org/writings/consoles/nes#bib:cpu-cpu), which is based on the popular 8-bit **MOS Technology 6502** and runs at **1.79 MHz** (or 1.66 MHz in PAL systems). This is the central component that executes the code inside the game cartridge.
### A bit of context
To understand the circuitry residing inside the NES’ motherboard, we must first take a look at the state of the industry at the time. Interestingly, the CPU market in the late 70s and early 80s was quite diverse.
[![Image](https://www.copetti.org/images/consoles/nes/pet.fb214c0d0cdb25a7353240a06f6f6534614d945e1886b4b7002f036e193f3c47_hu_91e54ab5b39b73dc.png)](https://www.copetti.org/images/consoles/nes/pet.fb214c0d0cdb25a7353240a06f6f6534614d945e1886b4b7002f036e193f3c47.webp)A Commodore PET, carrying a 6502 CPU.[![Image](https://www.copetti.org/images/consoles/nes/tandy.92e1450204bbb984bd7e04d23c9242c5c47f735e8519123a4013fbff1615a7f8_hu_45003284d1be99db.png)](https://www.copetti.org/images/consoles/nes/tandy.92e1450204bbb984bd7e04d23c9242c5c47f735e8519123a4013fbff1615a7f8.webp)A Tandy TRS-80, carrying a Z80 CPU.The panorama of late-70s computers, also provided by The Centre for Computing History (Cambridge, UK).
If you were a startup aiming to build an affordable microcomputer for the western world, you had plenty of options available:
  * The **Intel 8080** (1974): A popular CPU featured in the MITS Altair 8800, the first ‘personal’ computer. It comes with a modest 8-bit data bus, a 16-bit address bus (enough to handle the necessary memory), and seven 8-bit registers. With capabilities like this, a line was drawn between the simple calculator and an actual computer.
  * The **Zilog Z80** (1976): Displeased with Intel’s direction and lack of investment in their CPU division, former engineers of the 8080 started their own company to produce an ‘unofficial’ successor, enhanced with more instructions, registers, and internal components. To top it off, it was sold at a lower price and could still execute 8080 programs [[4]](https://www.copetti.org/writings/consoles/nes#bib:cpu-re_1977). The new CPU was well received by British firms Amstrad and Sinclair, as well as the Japanese [Sega](https://www.copetti.org/writings/consoles/master-system/), among others.
  * The **Motorola 6800** (1974): Another 8-bit CPU designed around the same time. While a direct competitor of the 8080, the 6800 was programmed using a more sophisticated instruction set, albeit running at a slower clock speed [[5]](https://www.copetti.org/writings/consoles/nes#bib:cpu-arizona). Nevertheless, many do-it-yourself computer kits, synthesisers, and all-in-one computers included the 6800.


Faced with similar setbacks that Intel’s employees went through, engineers at Motorola grew frustrated with the company’s lack of interest in capitalising on the potential of the 6800 [[6]](https://www.copetti.org/writings/consoles/nes#bib:cpu-austin). So, they joined a small but ambitious silicon firm, **MOS** , where they worked on a redesigned version of the 6800 - the **MOS 6502**. While incompatible with the rest, the new chip was much, _much_ cheaper to produce [[7]](https://www.copetti.org/writings/consoles/nes#bib:cpu-summary_costs) [[8]](https://www.copetti.org/writings/consoles/nes#bib:cpu-re_1981), and it was only a matter of time before iconic computer makers (Commodore, Tandy, Apple, Atari, Acorn, and so forth) chose the 6502 to power their machines.
Back in Japan, Nintendo needed something inexpensive yet familiar to develop for, so they selected the 6502. **Ricoh** , their CPU supplier, successfully produced a 6502-compatible clone.
### Core functionality
To understand how capable this console is, let’s first check what the original MOS 6502 offers:
  * The **6502 ISA** : MOS wanted to offer drastic improvements at the cost of compatibility with third-parties (especially Motorola) [[9]](https://www.copetti.org/writings/consoles/nes#bib:cpu-arizona). Thus, the 6502 instruction set still handles **8-bit** words like the 6800 and others, but its programming is not cross-compatible.
  * An **8-bit data bus** and a **16-bit address bus**. This was the typical combination for microprocessors of that era. Basically, it allows to operate data in chunks of eight bits without running out of memory locations (at least, too quickly).
    * On paper, 16-bit addresses means the 8-bit CPU will need extra cycles to process the extra size. However, thanks to MOS’s new addressing modes (explained further down), these penalties were alleviated without requiring too much circuitry.
  * **Three general-purpose registers** (`X`, `Y` and `A`), which may look constrained when compared to [larger register files](https://www.copetti.org/writings/consoles/master-system/#cpu). This decision reduces costs but also means the CPU would need to move memory around more frequently. With the 6502, `X` and `Y` are called ‘index registers’ and are used to address memory, while `A` is directly connected to the ALU and dedicated to arithmetic operations.
    * By comparison, the Motorola 6800 has two accumulator registers and only one index register, which allows for a simpler instruction set.
  * An **8-bit Arithmetic Logic Unit** (ALU), which comes as no surprise for an 8-bit CPU, but it’s worth pointing out that others like the Zilog Z80 came with an [4-bit ALU instead](https://www.copetti.org/writings/consoles/master-system/#cpu).
  * An **8-bit stack pointer** : This is usually beyond the scope of this analysis, but I wanted to highlight it due to its significant deviation from Motorola’s design. As mentioned before, the address bus is 16-bit, so a memory-dependent component like the stack pointer should ideally match that size. However, MOS opted to halve the requirement and store the stack within a fixed memory range. Nevertheless, it was a clever cost-saving measure, as it encouraged developers to adopt efficient programming techniques to maximise the stack space.
  * **13 addressing modes**. Thanks to the inclusion of two index registers, programs can choose between many formats for accessing memory. Some are optimised for zero-page addressing (the first 256 bytes of memory), while others encode a lookup address to retrieve the actual address dynamically. In the end, this helped save as many memory cycles as possible, at the cost of complexity.
    * By comparison, the 6800 and its single index register only offer seven addressing modes, with no equivalent for the flexible types.


As you can see, the remarkable engineering behind the 6502 allowed MOS to sell a compelling product at an extremely affordable price.
#### Ricoh’s licensing enigma
_How_ Ricoh managed to clone the 6502 isn’t clear to this day. One would expect MOS to have licensed the chip design to Ricoh, but there are many contradictions to this:
  * Both Ricoh’s and MOS’s variants feature the same layout, but Ricoh’s contains severed buses (disabling certain functions) [[10]](https://www.copetti.org/writings/consoles/nes#bib:cpu-differences). I go into more detail later.
  * A document explicitly stating that MOS licensed the 6502 to Ricoh is yet to be found.
  * An article published in 2008 by Nikkei Trendy states that Ricoh licensed from Rockwell, an authorised chip manufacturer [[11]](https://www.copetti.org/writings/consoles/nes#bib:cpu-trendi). However, it’s debatable whether a second source was able to provide IP to a third party, much less with MOS’s approval.
  * It wouldn’t be the first time Nintendo got away with circumventing IP rights, as _Ikegami Tsushinki v. Nintendo_ ruled in Japan that Nintendo didn’t own the code of the original Donkey Kong [[12]](https://www.copetti.org/writings/consoles/nes#bib:cpu-dk).


#### Scrapped functions
The Ricoh 2A03 omits the **Binary-Coded Decimal** (BCD) mode originally included in the 6502 [[13]](https://www.copetti.org/writings/consoles/nes#bib:cpu-visualbcd). BCD encodes each decimal digit of a number as a separate 4-bit binary. The 6502 uses 8-bit ‘words’ - meaning that each word stores two decimal digits.
As an example for the curious, the decimal number `42` is represented as:
  * `0010 1010` in binary.
  * `0100 0010` in BCD.


We could go on and on talking about it, but to give an outline: BCD is useful for applications that require treating each decimal place separately (for instance, a digital clock). However, it requires more storage since each 8-bit word can only encode up to the decimal number `99` - whereas traditional binary can encode up to `255`.
In any case, Ricoh deliberately broke BCD mode in its chip by severing the control lines that activate it. This was presumably done to avoid paying royalties to MOS, since BCD was patented by them (and the legislation that enabled copyrighting integrated circuit layouts in the United States wasn’t enacted until 1984 [[14]](https://www.copetti.org/writings/consoles/nes#bib:cpu-protection_act)).
### Memory
Both Ricoh 2A03 and MOS 6502 feature an **8-bit data bus** and a **16-bit address bus** , which allow them to access up to **64 KB of memory**. So, how did Nintendo fill that memory space?
On one side, the motherboard contains a chip providing **2 KB of Static RAM** (SRAM) [[15]](https://www.copetti.org/writings/consoles/nes#bib:cpu-sample_ram). Nintendo calls this area ‘Work RAM’ (WRAM) and can be used to store:
  * Variables for handling the game state and/or to look up information.
  * The ‘stack’, which temporarily saves register values while the CPU is executing subroutines.
  * A ‘buffer area’ so the CPU can copy large data between two locations.


On the other side, the components of the system are **memory-mapped** [[16]](https://www.copetti.org/writings/consoles/nes#bib:cpu-cpu_map), meaning that they are accessed using memory addresses and therefore occupy part of the CPU’s address space. Consequently, the Ricoh 2A03’s memory space is filled with addresses pointing to the game cartridge, WRAM, the PPU, the APU and two controllers (don’t worry about each component, as they are explained throughout this article).
#### Segmentation Fault
Inherited from MOS’ design, this console also features a special ‘anomaly’ called **Open Bus** : If an instruction tries to read from an unmapped or invalid address, the last value read is supplied instead [[17]](https://www.copetti.org/writings/consoles/nes#bib:nes-open_bus). If this goes unhandled by the program, execution may continue in an unpredictable state.
#### Cartridge/game data
Just in case you don’t know, NES games are distributed in the form of **cartridges** , and the cartridge’s buses connect directly to the CPU.
Nintendo wired up the cartridge lines in a way that only 49120 Bytes (~ 49.97 KB) of cartridge data can be accessed [[18]](https://www.copetti.org/writings/consoles/nes#bib:cpu-cpu_map). Now, what do I mean by ‘cartridge data’? Well, any chip connected to those buses, for instance:
  * A **Program ROM** where the game’s program resides. This excludes the graphics data, as you’ll later see in the ‘Graphics’ section. Naturally and unlike the other chips, this one is mandatory.
  * **RAM chips** to extend WRAM.
  * A **battery-packed RAM chip** to store saves.


The existence of different combinations stems from the fact that the CPU doesn’t care about what kind of component it is reading from; it only sees memory locations. So, it is up to game studios to choose (or devise) a feasible layout to fit in their game.
  * [Original](https://www.copetti.org/writings/consoles/nes#nestedtab-1-1-original)
  * [Marked](https://www.copetti.org/writings/consoles/nes#nestedtab-1-2-marked)

[![Image](https://www.copetti.org/images/consoles/nes/nrom.b4be7609d15f9dfee3498325efbfacc75efc9629ea841c18d6288902eede7a71.png)](https://www.copetti.org/images/consoles/nes/nrom.b4be7609d15f9dfee3498325efbfacc75efc9629ea841c18d6288902eede7a71.png)PCB of Super Mario Bros [[19]](https://www.copetti.org/writings/consoles/nes#bib:photography-nrom).[![Image](https://www.copetti.org/images/consoles/nes/nrom_marked.272d917f53f92b089c20b0a104fb8c2f73cfd0b5516b5d0b1fe88fca9ef24fd1.png)](https://www.copetti.org/images/consoles/nes/nrom_marked.272d917f53f92b089c20b0a104fb8c2f73cfd0b5516b5d0b1fe88fca9ef24fd1.png)The same PCB with important parts labelled. The meaning of the ‘Lockout’ chip is explained in the ‘Anti-piracy’ section.
For example, Nintendo’s ‘Super Mario Bros’ used a layout they call _NES-NROM-256_ and consists of 32 KB of program ROM and 8 KB of ‘Character ROM’ for graphics (we’ll see more about it in the ‘Graphics’ section) [[20]](https://www.copetti.org/writings/consoles/nes#bib:cpu-nrom). _NES-NROM-256_ was also prepared to house up to 3 KB of extra WRAM, though the game doesn’t make use of it.
#### Going beyond existing capabilities
One of the major limitations of 16-bit address buses (affecting 3rd and 4th-generation consoles) is their compact address space. Nowadays, 32-bit computers can address up to 4 GB of memory (and 64-bit machines lavishly enjoy up to 16 exabytes), so this is no longer a concern, but back then, the NES only had a 64 KB address space, and a significant portion was consumed by the memory-mapped hardware (something [competitors avoided](https://www.copetti.org/writings/consoles/master-system/#accessing-the-rest-of-the-components)).
So, did this mean that game studios could only develop games that stayed within the 49.97 KB limit? Absolutely not! If history has taught us anything, it is that there’s always a clever solution to a challenging problem, and this issue was tackled with a **Mapper**.
  * [With mapper](https://www.copetti.org/writings/consoles/nes#nestedtab-2-1-with-mapper)
  * [Without mapper](https://www.copetti.org/writings/consoles/nes#nestedtab-2-2-without-mapper)

[![Image](https://www.copetti.org/images/consoles/nes/_diagrams/mapper/mapper.ce712cf90024e048a2a2566df581e02584e11d7684f986fa508ce746a3e09cbc.png)](https://www.copetti.org/images/consoles/nes/_diagrams/mapper/mapper.ce712cf90024e048a2a2566df581e02584e11d7684f986fa508ce746a3e09cbc.png)Simplified representation of how a mapper extends the addressing capabilities of the CPU. With the inclusion of a mapper, the CPU can access extra banks (groups of addresses) of a large Program ROM. Although the game/program has the new task of manually switching between banks whenever needed.[![Image](https://www.copetti.org/images/consoles/nes/_diagrams/mapper/no_mapper.912a9dbb44efa4b4e599f53960b045930d7dfb6ddf071b4f3a94d02067f5c153.png)](https://www.copetti.org/images/consoles/nes/_diagrams/mapper/no_mapper.912a9dbb44efa4b4e599f53960b045930d7dfb6ddf071b4f3a94d02067f5c153.png)The same setup but without a mapper installed. While simpler and inexpensive, the CPU can only access a finite number of banks.
A mapper is an extra chip included in the cartridge that sits between the memory chips and the console’s address lines. Its primary job is to extend the address space, allowing developers to fit more chips. This is achieved through **bank switching** : memory addresses are grouped into banks, and the mapper provides switches (controlled via memory addresses) to alternate between them. Now, the CPU still perceives the same amount of memory, so it is the game (programmed with a mapper present) in charge of operating it. Due to their cost-effectiveness, mappers were the order of the day in 80s-to-early-90s technology.
  * [Original](https://www.copetti.org/writings/consoles/nes#nestedtab-3-1-original)
  * [Marked](https://www.copetti.org/writings/consoles/nes#nestedtab-3-2-marked)

[![Image](https://www.copetti.org/images/consoles/nes/tsrom.b8bbb5d13834500682896fda3682e41a70aca6a00bde14c9e0e7df04e9537e55.png)](https://www.copetti.org/images/consoles/nes/tsrom.b8bbb5d13834500682896fda3682e41a70aca6a00bde14c9e0e7df04e9537e55.png)PCB of Super Mario Bros 2 [[21]](https://www.copetti.org/writings/consoles/nes#bib:photography-tsrom). Super Mario Bros 3 also uses this layout but bundles a 256 KB Program ROM instead.[![Image](https://www.copetti.org/images/consoles/nes/tsrom_marked.d7d3bae32bf8ea63384aef5eb331a91956fbba1cd1f303f6b11aab74b0a7a957.png)](https://www.copetti.org/images/consoles/nes/tsrom_marked.d7d3bae32bf8ea63384aef5eb331a91956fbba1cd1f303f6b11aab74b0a7a957.png)The same picture with important parts labelled. At first, I thought the extra WRAM was for storing saves, but then I realised there are no saves in this game (and there isn’t a battery either). In reality, that RAM chip is used to store a decompressed level.
Back to the NES, games like ‘Super Mario Bros 2’ and ‘Super Mario Bros 3’ shipped with the ‘MMC3’ mapper (made by Nintendo) in their cartridges. For comparison, MMC3 provided up to 512 KB of space for the Program ROM, up to 256 KB for Character memory and up to 8 KB for extra WRAM [[22]](https://www.copetti.org/writings/consoles/nes#bib:cpu-mmc3). You can now see why ‘Super Mario Bros 3’ differs significantly in quality compared to the first instalment.
All in all, while this console may appear limited while examining its internal features, Nintendo made sure it could adapt as technology evolves. On the other side, while this technique helped to keep the costs down of the console, it shifted part of the burden to the game cartridge. So, game quality and cartridge costs were two concerns game studios had to balance.
* * *
## Graphics
Graphics are generated by a proprietary chip called the **Picture Processing Unit** (PPU). This is one of the chips that gives the NES an _identity_. To put it another way, since anyone could pick up a 6502 at a hardware store, why is the NES any different from, say, an Apple II or a Commodore 64? Well, what distinguishes the NES from other machines are the chips that surround the CPU: the PPU and the APU. These make up the NES’ unique graphics and audio capabilities, respectively.
[![Image](https://www.copetti.org/images/consoles/nes/ppu_chip.8fcd47f5d796ddef2bb4d8baa534306df6d7b81668b4af6b90157f0d32194da6_hu_6e8e279b6737c82.png)](https://www.copetti.org/images/consoles/nes/ppu_chip.8fcd47f5d796ddef2bb4d8baa534306df6d7b81668b4af6b90157f0d32194da6.webp)The European PPU chip on my NES’ motherboard.
That being said, the PPU renders 2D graphics called **sprites** and **backgrounds** , outputting the result to the video signal.
### Organising the content
[![Image](https://www.copetti.org/images/consoles/nes/_diagrams/ppu.8ca545d7ec1fbf59e628d4b670b565f94757f79b656f35f1140261794b4014f4.png)](https://www.copetti.org/images/consoles/nes/_diagrams/ppu.8ca545d7ec1fbf59e628d4b670b565f94757f79b656f35f1140261794b4014f4.png)Memory architecture of the PPU.
To render something on the screen, the PPU must know _which_ graphics to draw, _where_ on the screen to place them, and _how_ to draw them (i.e., which palette to use).
To answer these questions, the PPU came pre-programmed with a different memory layout that looks for specific types of data:
  * Graphics data is pulled from the game cartridge, which contains a dedicated chip called **Character memory** that stores the 2D drawings (called **tiles**) organised into a data structure named **Pattern table**. Character memory materialises in the form of ‘Read-Only Memory’ (ROM) or ‘Random-Access Memory’ (RAM), depending on whether the game ships with an immutable set of graphics or the CPU must intervene, respectively.
    * The PPU addresses **up to 8 KB** of Character memory organised into two groups of 4 KB each.
  * Meta-data telling the PPU ‘where’ and ‘how’ to draw graphics is found in other areas:
    * The motherboard houses **2 KB of SRAM** specifically for graphics-related data. Nintendo calls this space **Video RAM** (VRAM), and it stores two data structures called **Nametables**.
    * The PPU embeds **256 bytes** of DRAM to store the **Object Attribute Memory** (OAM).
    * Lastly, the PPU also bundles **4 bytes** of memory to define colour palettes.


Don’t worry about the new terminology; the meanings of these data structures are discussed step by step in the following paragraphs.
### Constructing the frame
As with its contemporaries, this chip is designed for the behaviour of a CRT display. There is no frame buffer as such: **the PPU will render in step with the CRT’s beam** , building the image on the fly.
The PPU draws frames with a fixed dimension of **256x240 pixels** [[23]](https://www.copetti.org/writings/consoles/nes#bib:graphics-overscan). Alas, due to the discrepancies in analogue video standards across the world, the image will differ in appearance depending on the region of the appliance (NTSC or PAL) from which it is displayed. In a nutshell, NTSC televisions will crop the top and bottom edges to accommodate overscan (only ~224 scan-lines are visible), so these edges are considered ‘danger zones’ by developers when deciding where to place elements in the game. On the other hand, PAL tellies won’t crop the edges but will show extra black bars to fill the taller signal (PAL uses 288 scan-lines).
Behind the scenes, the frame output by the PPU is composed of two different layers. For demonstration purposes, let’s use _Super Mario Bros._ to show how this works:
  * [Tiles](https://www.copetti.org/writings/consoles/nes#tab-1-1-tiles)
  * [Background Layer](https://www.copetti.org/writings/consoles/nes#tab-1-2-background-layer)
  * [Sprite Layer](https://www.copetti.org/writings/consoles/nes#tab-1-3-sprite-layer)
  * [Background Split](https://www.copetti.org/writings/consoles/nes#tab-1-4-background-split)
  * [Result](https://www.copetti.org/writings/consoles/nes#tab-1-5-result)


#### Tiles
  * [All](https://www.copetti.org/writings/consoles/nes#nestedtab-4-1-all)
  * [Single](https://www.copetti.org/writings/consoles/nes#nestedtab-4-2-single)

[![Image](https://www.copetti.org/images/consoles/nes/ppu_mario/chr_map.85c856cefd8daa4752b44b0fc04c9bc3e60ece2851f932bf64431dee293f54d2.png)](https://www.copetti.org/images/consoles/nes/ppu_mario/chr_map.85c856cefd8daa4752b44b0fc04c9bc3e60ece2851f932bf64431dee293f54d2.png)Two pattern tables with multiple tiles squashed together.![Image](https://www.copetti.org/images/consoles/nes/ppu_mario/single.cd333403bda182a98bc72773125dadee3055e8dbce200823039e09b7e12996f7.png)A single tile.Tiles Found in Character ROM (for demonstration purposes a default palette is being used).
To begin with, the PPU uses **tiles** as a basic ingredient for producing sprites and backgrounds.
The NES defines tiles as basic **8x8 pixel maps** , these are stored in **Character memory** (residing in the game cartridge) and organised into a big data structure called **Pattern Table** [[24]](https://www.copetti.org/writings/consoles/nes#bib:graphics-rust). Each tile occupies 16 bytes, and a Pattern table houses 256 tiles [[25]](https://www.copetti.org/writings/consoles/nes#bib:graphics-pattern). Since the PPU addresses up to 8 KB of Character memory, it can access up to two Pattern tables.
Inside a tile, each of its pixels is encoded using a 2-bit value, which references one of four colours from a palette. Programmers can define up to eight palettes (four for the background and four for sprites). The colours referenced on each palette point to a ‘master palette’ consisting of 64 colours [[26]](https://www.copetti.org/writings/consoles/nes#bib:graphics-palettes), representing all the colours that this console can produce. Each palette is made of four colours, with one reserved for `transparent`.
To start drawing something on the screen, games populate a set of tables with references to tiles stored in Character memory. Each table is responsible for one layer (sprite or background) of the frame. Then, the PPU reads from those tables and composes the scan-lines that will be beamed by the CRT gun.
I will now explain how each layer/table works and how they differ in terms of functionality.
« Previous [Next »](https://www.copetti.org/writings/consoles/nes#tab-1-2-background-layer)
#### Background Layer
  * [Overall](https://www.copetti.org/writings/consoles/nes#nestedtab-5-1-overall)
  * [Selected](https://www.copetti.org/writings/consoles/nes#nestedtab-5-2-selected)

[![Image](https://www.copetti.org/images/consoles/nes/ppu_mario/nametable.e0055ad58816fb592360356ed85e039010bf2d25f382922da0ec3c65f29c7153.png)](https://www.copetti.org/images/consoles/nes/ppu_mario/nametable.e0055ad58816fb592360356ed85e039010bf2d25f382922da0ec3c65f29c7153.png)Visualised background map.[![Image](https://www.copetti.org/images/consoles/nes/ppu_mario/nametable_marked.e0e520cc7636d1539f9798032e9c14882a79b49cadba9faf25bfece7ae19cbe3.png)](https://www.copetti.org/images/consoles/nes/ppu_mario/nametable_marked.e0e520cc7636d1539f9798032e9c14882a79b49cadba9faf25bfece7ae19cbe3.png)Visualised background with selected area marked.This background map is set up with vertical mirroring, which enables smooth horizontal scrolling. However, only the top half can be used.
The background layer is a 512x480 pixel map containing static tiles [[27]](https://www.copetti.org/writings/consoles/nes#bib:graphics-nametables). You may recall that the viewable frame is much smaller, so the game decides which part of the layer is selected for display. Games can also shift the viewable area during gameplay; that’s how the **scrolling effect** is accomplished.
To save memory, groups of four tiles are combined into 16x16-pixel maps called **blocks** , in which all tiles share a colour palette.
**Nametables** (stored in VRAM) specify which tiles to display in the background layer. The PPU looks for four 1024-byte Nametables, each one corresponding to a quadrant of the layer. However, only 2 KB of VRAM is available! Meaning that only two Nametables can be stored without additional hardware provided by the cartridge. Yet, the remaining two still have to be addressed somewhere: most games simply point the remaining two where the first two are (this is called **mirroring**).
Although this architecture may seem flawed at first, it was designed to minimise costs while ensuring simple **expandability** : if the game requires a wider background, just fit extra VRAM in the cartridge.
Moving on, the last bytes of each Nametable store a 64-byte **Attribute table** that specifies which colour palette is assigned to each block [[28]](https://www.copetti.org/writings/consoles/nes#bib:graphics-attribute_table).
[« Previous](https://www.copetti.org/writings/consoles/nes#tab-1-1-tiles) [Next »](https://www.copetti.org/writings/consoles/nes#tab-1-3-sprite-layer)
#### Sprite Layer
[![Image](https://www.copetti.org/images/consoles/nes/ppu_mario/sprite_layer.5be82835c348c3dff9873a74ab923877ff4b7bed75c333dbc4b38e190f3c7379.png)](https://www.copetti.org/images/consoles/nes/ppu_mario/sprite_layer.5be82835c348c3dff9873a74ab923877ff4b7bed75c333dbc4b38e190f3c7379.png)Rendered sprite layer.
Sprites are tiles that can move around the screen. They can also overlap one another, or appear behind the background. The viewable graphic is determined by its priority value (similar to the concept of ‘layers’ in traditional graphic design software).
The **Object Attribute Memory** (OAM) table specifies which tiles will be used as sprites [[29]](https://www.copetti.org/writings/consoles/nes#bib:graphics-oam). In addition to the tile index, each entry includes an (x,y) position and several attributes (colour palette, priority and flip flags). This table resides in a 256-byte DRAM located within the PPU chip.
The CPU can populate the OAM table, but this process can be slow in practice and risks corrupting the frame if not timed correctly. As a result, the PPU contains a small component called **Direct Memory Access** or ‘DMA’ which can be programmed (by altering the PPU’s registers) to fetch the table from WRAM. With DMA, the table is guaranteed to be uploaded when the next frame is drawn; however, the CPU will be halted during the transfer!
The PPU is limited to **eight sprites per scan-line** and up to **64 sprites per frame**. Luckily, the scan-line limit can be partially circumvented thanks to a technique called ‘OAM order rotation’, in which the game manually alters the order of entries in OAM. This makes the PPU render a different sprite set at each frame, and the speed of the CRT beam will trick the user into seeing more sprites than allowed. However, they will also appear to flicker on-screen.
[« Previous](https://www.copetti.org/writings/consoles/nes#tab-1-2-background-layer) [Next »](https://www.copetti.org/writings/consoles/nes#tab-1-4-background-split)
#### Background Split
[![Image](https://www.copetti.org/images/consoles/nes/ppu_mario/split.7d72639126de3ef8b96b676e2322591454aa1e938420a85e261f295ae007ab92.png)](https://www.copetti.org/images/consoles/nes/ppu_mario/split.7d72639126de3ef8b96b676e2322591454aa1e938420a85e261f295ae007ab92.png)Rendered background layer highlighting the two portions with different scrolling values defined. Only the second portion scrolls as Mario moves.
Before we move on, there’s an additional detail worth mentioning. If you play Super Mario Bros, you’ll notice that when Mario moves, the scene scrolls without a hitch. However, you’ll also observe that the top area (where the stats are) remains static **even though both portions belong to the same background layer!** So, what is happening here? Well, the game is altering the scrolling values mid-frame to show the overworld and the stats (residing in a fixed portion of the background) at the same time. The NES doesn’t provide this feature natively, but the game deduces the timings by observing the state of the PPU (manifested through its status register [[30]](https://www.copetti.org/writings/consoles/nes#bib:graphics-ppustatus)).
To accomplish this, games use a technique called **Sprite 0 Hit**. Super Mario Bros instructs the PPU to render a dummy sprite behind the coin, this happens to be the first sprite drawn within the frame. After the PPU beams it, it updates its status register with a flag to indicate that the first sprite (a.k.a ‘sprite 0’) has been drawn. Meanwhile, the game continuously checks mid-frame whether the sprite 0 status has been flagged (a.k.a ‘hit’). When this occurs, the game updates the scrolling value of the background table to align it with Mario’s position.
Overall, ‘Sprite 0 Hit’ is a very delicate procedure, as it’s easy to mess up the timings (sprite 0’s flag is not cleared after polling it, which leads to ‘duplicated’ positives [[31]](https://www.copetti.org/writings/consoles/nes#bib:graphics-chibiakumas)). Furthermore, as this routine repeats indefinitely, it can be quite costly (in terms of CPU cycles) to execute. On the bright side, later mappers took over this function by employing automatic interrupts that are triggered whenever an arbitrary scan-line is hit [[32]](https://www.copetti.org/writings/consoles/nes#bib:graphics-nesdoug) (a much more efficient technique), which significantly improved the visual capabilities of Super Mario Bros 3, for instance.
[« Previous](https://www.copetti.org/writings/consoles/nes#tab-1-3-sprite-layer) [Next »](https://www.copetti.org/writings/consoles/nes#tab-1-5-result)
#### Result
[![Image](https://www.copetti.org/images/consoles/nes/ppu_mario/result.b4d077e7fb855c96b087f8cb5fdda12a4eb258758320dd3cb747a4f8b0a55623.png)](https://www.copetti.org/images/consoles/nes/ppu_mario/result.b4d077e7fb855c96b087f8cb5fdda12a4eb258758320dd3cb747a4f8b0a55623.png)Tada!
Once the frame is finished, it’s time to move on to the next one!
However, the CPU can’t modify any table currently in use by the PPU, otherwise, artefacts may show up on the screen. So, when all scan-lines are completed, the PPU triggers the **Vertical Blank** (V-Blank) interrupt on the CPU [[33]](https://www.copetti.org/writings/consoles/nes#bib:graphics-vblank). This notifies the game that it can start updating the tables without tearing the picture currently displayed. At that moment, the CRT’s beam is pointing below the visible area of the screen, into the overscan (or bottom border area).
Only a handful of PPU registers can be updated outside the V-Blank window [[34]](https://www.copetti.org/writings/consoles/nes#bib:graphics-outside_vblank), which explains the ability to scroll the background layer mid-frame.
[« Previous](https://www.copetti.org/writings/consoles/nes#tab-1-4-background-split) Next »
### Secrets and limitations
If you’re thinking that a frame-buffer system with memory allocated to store the full frame would have been preferable: RAM costs were prohibitively high, and the console’s goal was to be affordable. Let me now show you why this design still proved to be both efficient and flexible.
  * [Multi-Scrolling](https://www.copetti.org/writings/consoles/nes#tab-2-1-multi-scrolling)
  * [Tile-Swapping](https://www.copetti.org/writings/consoles/nes#tab-2-2-tile-swapping)
  * [Curious behaviour](https://www.copetti.org/writings/consoles/nes#tab-2-3-curious-behaviour)


#### Multi-Scrolling
[![Image](https://www.copetti.org/images/consoles/nes/secrets/multiscrolling_mirror.69ee2c1e8f9336fb7c94b85f8e5ce5ed83f0f57f25bdb12c121bd1f7e755e99f.png)](https://www.copetti.org/images/consoles/nes/secrets/multiscrolling_mirror.69ee2c1e8f9336fb7c94b85f8e5ce5ed83f0f57f25bdb12c121bd1f7e755e99f.png)In this level of Super Mario Bros. 2, the Nametable is set up for vertical scrolling (horizontal mirroring).[![Image](https://www.copetti.org/images/consoles/nes/secrets/multiscrolling.0b5ffd79e4463beb3bffbbf8781de6be84fbfbaedbf2de370177527307cef6f1.png)](https://www.copetti.org/images/consoles/nes/secrets/multiscrolling.0b5ffd79e4463beb3bffbbf8781de6be84fbfbaedbf2de370177527307cef6f1.png)With Super Mario Bros. 3, Mario can run and fly. Thus, the PPU needs to scroll diagonally. Notice the right edge is showing the wrong colour palette, and the left edge has a mask applied.
Some games require the main character to move vertically; therefore, the nametable is set up with **horizontal mirroring**. Other games need their character to move left and right, and so implement **vertical mirroring** instead.
Either type of mirroring allows the PPU to update background tiles without the user noticing, as there is ample of space to scroll while new tiles are being rendered at a distance.
But what happens if the character needs to move diagonally? The PPU can scroll in any direction; however, without extra VRAM, the edges are forced to share the same colour palette (remember that tiles are grouped in blocks).
This explains why some games like _Super Mario Bros. 3_ show strange graphics at the right edge of the screen while Mario moves (the game is set up for vertical scrolling) [[35]](https://www.copetti.org/writings/consoles/nes#bib:graphics-seam). It’s possible that they needed to minimise the hardware cost per cartridge, as this game already bundles a powerful mapper.
As an interesting _fix_ : the PPU allowed developers to apply a vertical mask on top of tiles, effectively concealing part of the glitchy area.
« Previous [Next »](https://www.copetti.org/writings/consoles/nes#tab-2-2-tile-swapping)
#### Tile-Swapping
  * [Early](https://www.copetti.org/writings/consoles/nes#nestedtab-6-1-early)
  * [Late](https://www.copetti.org/writings/consoles/nes#nestedtab-6-2-late)
  * [Displayed](https://www.copetti.org/writings/consoles/nes#nestedtab-6-3-displayed)

[![Image](https://www.copetti.org/images/consoles/nes/secrets/multiplexing_1.d8e6b0730b39458e7d6306c71b3a75c559b4e4bdc8ea7542be7c323d05f856e6.png)](https://www.copetti.org/images/consoles/nes/secrets/multiplexing_1.d8e6b0730b39458e7d6306c71b3a75c559b4e4bdc8ea7542be7c323d05f856e6.png)Early scan lines.[![Image](https://www.copetti.org/images/consoles/nes/secrets/multiplexing_2.caf48911e860280c482d8264f49007d9d3b1efafbee0f26024be7ff1a1f65395.png)](https://www.copetti.org/images/consoles/nes/secrets/multiplexing_2.caf48911e860280c482d8264f49007d9d3b1efafbee0f26024be7ff1a1f65395.png)Late scan lines.[![Image](https://www.copetti.org/images/consoles/nes/secrets/multiplexing_complete.316fb464f79dfeab19f2f9769cc152185d5c9401f8210dd8ffb2ac4ed429d820.png)](https://www.copetti.org/images/consoles/nes/secrets/multiplexing_complete.316fb464f79dfeab19f2f9769cc152185d5c9401f8210dd8ffb2ac4ed429d820.png)Actual frame displayed to the user.Hypothetical frames rendered using tiles available during specific scan lines.
Another remarkable feature of Super Mario Bros. 3 is the number of graphics it can display.
This game displays more background tiles than strictly permitted. How does it achieve this? By taking two screen captures at different times while the display is generated, we can see that the final frame is actually composed of _two_ distinct frames.
This is another wizardry of the MMC3 mapper, which not only addresses extra space in the Program ROM, but also extends the Character ROM space by connecting **two separate Character chips**. By determining which part of the screen the PPU is requesting, the mapper redirects to one chip or the other, thereby allowing more unique tiles on-screen than was originally supported [[36]](https://www.copetti.org/writings/consoles/nes#bib:graphics-n3s).
[« Previous](https://www.copetti.org/writings/consoles/nes#tab-2-1-multi-scrolling) [Next »](https://www.copetti.org/writings/consoles/nes#tab-2-3-curious-behaviour)
#### Curious behaviour
Throughout my research, I came across many interesting articles that explain unusual behaviour of the PPU, so I thought to mention a few here:
  * Unlike the [Master System’s VDP](https://www.copetti.org/writings/consoles/master-system/#graphics), which generates RGB colours that are subsequently encoded into NTSC/PAL signals for broadcasting, the **NES’ PPU does all at once** [[37]](https://www.copetti.org/writings/consoles/nes#bib:graphics-palettes). Hence, there isn’t a one-to-one correspondence between the colours of the PPU master palette and the standard RGB colourspace (widely adopted by present technology). This leaves some room for interpretation and, as a consequence, various emulators may display a different palette.
    * The discrepancies between RGB palettes can be observed using Tim Worthington’s DIY kit, which adds RGB signal output to the NES. This also houses a switch to choose between three predefined palettes [[38]](https://www.copetti.org/writings/consoles/nes#bib:graphics-nesrgb).
  * The master palette contains a **‘cursed’ colour** (`$0D`), which might disrupt the NTSC TV signal [[39]](https://www.copetti.org/writings/consoles/nes#bib:graphics-cursed_colour). Well, what happens is that some TVs mistake the signal for displaying that colour as the blanking signal, which may cause flickering.
  * The PPU relies on DRAM to store its Object Attribute Memory (OAM). Now, unlike SRAM, DRAM must be refreshed constantly to prevent data loss. Conversely, **the PPU doesn’t refresh DRAM when it’s not rendering the frame** [[40]](https://www.copetti.org/writings/consoles/nes#bib:graphics-oam). This typically occurs during vertical blanking. For this reason, it is advised to always update OAM during vertical blanking, since the non-refreshing period (happening during V-blank) will have corrupted part of the table.
    * The PPU variant for PAL systems is unaffected by this, as it does refresh during V-Blank (which lasts longer on PAL systems).


[« Previous](https://www.copetti.org/writings/consoles/nes#tab-2-2-tile-swapping) Next »
* * *
## Audio
A dedicated component called **Audio Processing Unit** (APU) provides this service [[41]](https://www.copetti.org/writings/consoles/nes#bib:audio-apu). Ricoh embedded it inside the CPU chip, presumably to prevent unlicensed cloning of both the CPU and APU.
### Functionality
This audio circuitry is commonly referred to as a **Programmable Sound Generator** (PSG), which vaguely implies that it can only produce a predefined set of waveforms. This is _mostly_ true in this case.
The APU sequences audio data across **five channels** , each reserved for a specific waveform or signal. The channels contain different properties that alter the waveform’s pitch, sound, volume and duration. They are continuously mixed and transmitted through the output audio signal.
The APU’s functionality is exposed through memory addresses. The CPU reads the music-related data found in the Program ROM and programs the APU accordingly.
Furthermore, the Famicom model implements extra cartridge pins that send the mixed audio signal to the cartridge, so the latter can mix it with **extra channels** (requiring additional chips) [[42]](https://www.copetti.org/writings/consoles/nes#bib:general-cartridge).
Let’s now review the five channels the APU provides [[43]](https://www.copetti.org/writings/consoles/nes#bib:audio-review):
  * [Pulse](https://www.copetti.org/writings/consoles/nes#tab-3-1-pulse)
  * [Triangle](https://www.copetti.org/writings/consoles/nes#tab-3-2-triangle)
  * [Noise](https://www.copetti.org/writings/consoles/nes#tab-3-3-noise)
  * [Sample](https://www.copetti.org/writings/consoles/nes#tab-3-4-sample)


#### Pulse
  * [Pulse 1](https://www.copetti.org/writings/consoles/nes#nestedtab-7-1-pulse-1)
  * [Pulse 2](https://www.copetti.org/writings/consoles/nes#nestedtab-7-2-pulse-2)
  * [Complete](https://www.copetti.org/writings/consoles/nes#nestedtab-7-3-complete)

No support for video.Pulse 1 channel. No support for video.Pulse 2 channel. No support for video.All audio channels.Oscilloscope display of a music score from Mother (1989).
The first **two channels** produce **pulse waves** [[44]](https://www.copetti.org/writings/consoles/nes#bib:audio-apupulse). When heard, they exhibit a very distinct _beep_ sound that is mainly used for **melody or sound effects**. By varying the pulse width (also known as the **duty cycle**), the respective sequencer can generate three types of pulse waves. The circuits are also connected to a **sweep unit** (allowing to bend the pitch) and an **envelope generator** to lower the volume over time (commonly referred to as **decay**).
Most games use one pulse channel for melody and the other for accompaniment. You’ll often find that when a game needs to play a sound effect, the accompaniment channel is temporarily switched to play the effect before returning to its original role. This prevents interrupting the melody during gameplay.
I believe it’s fair to say that pulse waves are one of the emblems of this generation of consoles. I assume their adoption was primarily driven by cost-effectiveness: the (limited) CPU can only process a finite amount of data at a time, and pulse waves are ideal because they require few parameters to play simple melodies (which, in turn, frees up CPU cycles for other operations).
« Previous [Next »](https://www.copetti.org/writings/consoles/nes#tab-3-2-triangle)
#### Triangle
  * [Triangle](https://www.copetti.org/writings/consoles/nes#nestedtab-8-1-triangle)
  * [Complete](https://www.copetti.org/writings/consoles/nes#nestedtab-8-2-complete)

No support for video.Triangle channel. No support for video.All audio channels.Oscilloscope display of a music score from Mother (1989).
One of the specialities of the APU, when compared to the competition, is its ability to produce **triangle waves**. These are often used as a **bassline** for melodies. Additionally, by dramatically modifying its pitch, it can also be used for **percussion**.
The APU has one channel reserved for this type of wave. Behind the scenes, a dedicated sequencer takes 32 cycles to generate a triangle signal [[45]](https://www.copetti.org/writings/consoles/nes#bib:audio-aputriangle); this limitation causes the resulting triangle waveform to resemble a step ladder.
On the other side, the respective circuitry does not provide volume control. In any case, some games discovered alternative methods by fiddling with the mixer’s volume control.
[« Previous](https://www.copetti.org/writings/consoles/nes#tab-3-1-pulse) [Next »](https://www.copetti.org/writings/consoles/nes#tab-3-3-noise)
#### Noise
  * [Noise](https://www.copetti.org/writings/consoles/nes#nestedtab-9-1-noise)
  * [Complete](https://www.copetti.org/writings/consoles/nes#nestedtab-9-2-complete)

No support for video.Noise channel. No support for video.All audio channels.Oscilloscope display of a music score from Mother (1989).
The concept of ‘Noise’ refers to a series of waveforms that lack any discernible pattern or order. In turn, our ears interpret it as white static. That said, the APU allocates one channel to play different kinds of noise.
Behind the scenes, the noise generator relies on an envelope generator (similar to the Pulse channel) that is randomly muted by an OR gate [[46]](https://www.copetti.org/writings/consoles/nes#bib:audio-apunoise). The condition for muting is determined by the value of a 15-bit shift register connected to a feedback loop. All in all, this makes the circuitry output a signal with _pseudo-unpredictable_ patterns, resulting in noise.
For control, four bits adjust the period of the envelope generator, while one bit modifies the ‘Mode’ of the shift register. This layout provides 32 noise presets. Half (16) of these presets generate **clean static** , and the other half produce **robotic static**.
Generally speaking, games utilise the noise channel for percussion or ambient effects.
[« Previous](https://www.copetti.org/writings/consoles/nes#tab-3-2-triangle) [Next »](https://www.copetti.org/writings/consoles/nes#tab-3-4-sample)
#### Sample
  * [Sample](https://www.copetti.org/writings/consoles/nes#nestedtab-10-1-sample)
  * [Complete](https://www.copetti.org/writings/consoles/nes#nestedtab-10-2-complete)

No support for video.Sample channel. No support for video.All audio channels.Oscilloscope display of a music score from Mother (1989).
Samples are recorded pieces of music that can be replayed. As you can see, samples are not confined to a single waveform, but they consume a lot more storage space.
The APU has one channel dedicated to samples. Here, samples are limited to **7-bit resolution** (encoded with values from `0` to `127`) and a **~15.74 kHz sampling rate** [[47]](https://www.copetti.org/writings/consoles/nes#bib:audio-2a03ref). To program this channel, games can either stream 7-bit values (which steals significant cycles and storage) or use **delta modulation** to encode only the variation between consecutive samples.
The delta modulation system in the APU only accepts 1-bit values, meaning games can only indicated whether the sample increments or decrements by `1` each time the counter kicks in. Thus, at the cost of fidelity, delta modulation can save games from having to stream continuous values to the APU.
Since programming this channel takes longer space and CPU cycles, games typically store small pieces (like drum sounds) that can be replayed repeatedly. Be as it may, throughout the NES’ lifespan, numerous developers have come up with clever uses for this channel.
[« Previous](https://www.copetti.org/writings/consoles/nes#tab-3-3-noise) Next »
### Secrets and limitations
While the APU could not match the audio quality of vinyl, cassette or CD, programmers did find ways to extend its capabilities, largely thanks to the modular architecture of the NES.
  * [Extra Channels](https://www.copetti.org/writings/consoles/nes#tab-4-1-extra-channels)
  * [Tremolo](https://www.copetti.org/writings/consoles/nes#tab-4-2-tremolo)


#### Extra Channels
  * [American](https://www.copetti.org/writings/consoles/nes#nestedtab-11-1-american)
  * [Japanese](https://www.copetti.org/writings/consoles/nes#nestedtab-11-2-japanese)

No support for video.Castlevania III (USA/Europe, 1989). No support for video.Akumajō Densetsu (Japan, 1989).Oscilloscope display of the same music score across the two regions.
Remember that the Famicom provided exclusive cartridge pins available for sound expansion? Well, games like _Castlevania 3_ took advantage of this feature by incorporating an additional chip called **Konami VRC6** , which introduced **two extra pulse waves and a sawtooth wave** to the mix.
The two examples illustrate the difference between the Japanese and the American versions of the game. The Japanese variant, running on the Famicom, benefits from the enhanced audio capabilities, while the American version, designed for the NES, is constrained by the five predefined channels.
« Previous [Next »](https://www.copetti.org/writings/consoles/nes#tab-4-2-tremolo)
#### Tremolo
No support for video.Oscilloscope view of Final Fantasy III (1990).
Rather than increasing cartridge costs, some games prioritised creativity over technology to simulate additional channels.
For instance, Final Fantasy III came up with the idea of using tremolo effects to create the illusion of extra channels.
[« Previous](https://www.copetti.org/writings/consoles/nes#tab-4-1-extra-channels) Next »
### A more refined observation
Now that you’ve had a glimpse of what the APU is capable of, let me show you a more precise method for observing how its sound behaves. This will not only complement what you already know about the APU but also provide a more objective examination.
First things first, let’s start with a brief introduction to sound theory.
Thanks to the principles of **Fourier Analysis** , we can decompose every single sound we hear into a **sum of sine waves** with different frequencies and amplitudes [[48]](https://www.copetti.org/writings/consoles/nes#bib:audio-complexwaveforms). The lowest-frequency sine wave is called the **fundamental** , while the others are referred to as **overtones**. If you add the fundamental wave and its overtones, you get the original sound back. Having said that, with sounds that have a recognisable pitch, you’ll find most (if not all) overtones have frequencies that are multiples of the fundamental frequency. Thus, these overtones are called **harmonics** [[49]](https://www.copetti.org/writings/consoles/nes#bib:audio-harmonics).
Harmonics will be a recurring topic in this section, as waveforms such as pulses, triangles, and sawtooths adhere to a formula that determines the harmonics they must contain. Otherwise, these waveforms might deviate from their ‘perfect’ shape.
#### Introduction to spectrograms
As sine waves are now the key ingredient that can make up any sound, we can now analyse the sounds that we hear by their sine waves. Now, for any kind of data analysis, there’s nothing more convenient than plotting a graph to organise vast amounts of information. Well, in the case of sound analysis, we’ve got **Spectrograms**. These encode all the information from an audio sample in a single plot. The X-axis denotes time (in seconds), the Y-axis denotes the frequencies (in Hz) of sine waves produced during that time, and the Z-axis (intensity of each dot) denotes the power/loudness (in decibels) of each frequency.
No support for video.Example of spectrogram visualising six seconds of a Pulse channel.
As you can observe from this example, each horizontal line (a.k.a. sequences of dots) corresponds to a sine wave (the lowest is the fundamental, while the rest are the harmonics) and their intensity indicates the amplitude. With this in mind, we can extract the following information:
  * Over time, horizontal lines tend to drastically displace. That’s the pitch of the Pulse channel changing.
  * The start of each note is loud (the dots are vibrant) followed by a quick quell. That’s the APU’s envelope control in action.
    * Moreover, at the end of the decay period, a vertical line shows up. It’s quite brief so it’s not easily audible but, in any case, that’s noise (a short popping sound) and I suspect it’s a deficiency of the APU.
  * Holding a note for more than 0.25 seconds makes **vibrato** emerge (continuous fluctuations in the Y-axis). I’m not sure if that’s intentional (using the sweep function) or an adverse effect of the APU.


Notice how most of these observations are not easily derived by just listening to an audio sample; this is the reason for writing this section.
#### Plotting the APU
To study the NES’ APU, I’ve compiled five spectrograms, each corresponding to one of the APU’s channels, using the previous examples. Alongside them, you’ll find my attempt at unravelling what the data is exhibiting.
Before we start, I must confess that, to gather the data without inaccuracies (such as extra noise), some compromises were made. The recordings were obtained using a Windows program called ‘towave’, which uses **band-limited synthesis** to solve a fundamental problem with the emulation of PSG-based audio chips. Essentially, pulses, triangles and sawtooths consist of **infinite harmonics**. However, this doesn’t mix well with modern sound cards which are limited to 44.1 kHz samples. Thus, a technique called ‘band-limited synthesis’ is employed to select the right harmonics within the sound card’s limitations. All in all, this technique provides a feasible balance between performance, accuracy, and aliasing prevention. However, the data may not be 100% identical to its analogue counterpart (which, by contrast, would also introduce other issues, like noise from the recording equipment), but I believe it is to an acceptable degree and, most importantly, does the job for this section of the article.
That being said, let’s get on with the analysis.
  * [Pulse](https://www.copetti.org/writings/consoles/nes#tab-5-1-pulse)
  * [Triangle](https://www.copetti.org/writings/consoles/nes#tab-5-2-triangle)
  * [Noise](https://www.copetti.org/writings/consoles/nes#tab-5-3-noise)
  * [Sample](https://www.copetti.org/writings/consoles/nes#tab-5-4-sample)
  * [Sawtooth](https://www.copetti.org/writings/consoles/nes#tab-5-5-sawtooth)


##### Pulse
[![Image](https://www.copetti.org/images/consoles/nes/spectrograms/eb0_pulse_nes.3a55c1442998128eb5f5f9bc6dbc4660577f91eb10816acdbe57dcb8d01b45f2.png)](https://www.copetti.org/images/consoles/nes/spectrograms/eb0_pulse_nes.3a55c1442998128eb5f5f9bc6dbc4660577f91eb10816acdbe57dcb8d01b45f2.png)Spectrogram of the Pulse 1 channel.
The theory says that a pulse tone only contains odd harmonics. In other words, the fundamental is combined with its third harmonic, fifth and so forth. Moreover, each harmonic decreases its amplitude the further it is from the fundamental. The amplitude formula is `amplitude = 1 ÷ harmonic number` [[50]](https://www.copetti.org/writings/consoles/nes#bib:audio-pulse).
Hence, notice how the intensity of each harmonic on the spectrogram dims the higher it is on the Y-axis. However, the APU’s pulse waves also seem to exhibit the aforementioned vibrato effect which intensifies at each harmonic number. Moreover, areas of the spectrogram that should be empty of any sound contain hushed overtones (possibly the result of noise and other imperfections).
« Previous [Next »](https://www.copetti.org/writings/consoles/nes#tab-5-2-triangle)
##### Triangle
[![Image](https://www.copetti.org/images/consoles/nes/spectrograms/eb0_triangle_nes.aba5614553cf6f43d5409f512e922a9d988457ba37447c8765cd18a858d765b6.png)](https://www.copetti.org/images/consoles/nes/spectrograms/eb0_triangle_nes.aba5614553cf6f43d5409f512e922a9d988457ba37447c8765cd18a858d765b6.png)Spectrogram of the Triangle channel.
A triangle wave is also made of odd harmonics, but their amplitude decreases more rapidly (following the formula `amplitude = 1 ÷ harmonic number²` [[51]](https://www.copetti.org/writings/consoles/nes#bib:audio-triangle)).
However, this is not what is shown here. The step-ladder-shaped triangle that the APU produces introduces additional harmonics and increased amplitudes.
[« Previous](https://www.copetti.org/writings/consoles/nes#tab-5-1-pulse) [Next »](https://www.copetti.org/writings/consoles/nes#tab-5-3-noise)
##### Noise
[![Image](https://www.copetti.org/images/consoles/nes/spectrograms/eb0_noise_nes.26c37982c3dffd5dcaed5650f484b5265a2a7c98aaa6bbfb1864ef5f4fb35a91.png)](https://www.copetti.org/images/consoles/nes/spectrograms/eb0_noise_nes.26c37982c3dffd5dcaed5650f484b5265a2a7c98aaa6bbfb1864ef5f4fb35a91.png)Spectrogram of the Noise channel.
Naturally, noise doesn’t abide by the rules of harmonics and may randomly fill the entire frequency spectrum, hence the absence of a clearly recognisable pitch.
Although, by observing the timeline, you can distinguish between the various noise presets provided by the APU, each exhibiting a unique set of overtones.
[« Previous](https://www.copetti.org/writings/consoles/nes#tab-5-2-triangle) [Next »](https://www.copetti.org/writings/consoles/nes#tab-5-4-sample)
##### Sample
[![Image](https://www.copetti.org/images/consoles/nes/spectrograms/eb0_dcm_nes.209437b721ccf3925eb08576807df50248015103c84f23ed7128514bce27856d.png)](https://www.copetti.org/images/consoles/nes/spectrograms/eb0_dcm_nes.209437b721ccf3925eb08576807df50248015103c84f23ed7128514bce27856d.png)Spectrogram of the Sample channel.
Unlike the previous channels, the sample channel only plays back whatever low-resolution recording the developer feeds to the APU. Considering the example played a drum kit, I can’t see any identifiable treats on the spectrogram (apart from similarities to white noise).
[« Previous](https://www.copetti.org/writings/consoles/nes#tab-5-3-noise) [Next »](https://www.copetti.org/writings/consoles/nes#tab-5-5-sawtooth)
##### Sawtooth
[![Image](https://www.copetti.org/images/consoles/nes/spectrograms/castlevania_saw_nes.c160d3b5480b311b87ff18d8f80f6ec6e846829bceb908e9bbf812484c33fafb.png)](https://www.copetti.org/images/consoles/nes/spectrograms/castlevania_saw_nes.c160d3b5480b311b87ff18d8f80f6ec6e846829bceb908e9bbf812484c33fafb.png)Spectrogram of the VRC6’s Sawtooth channel.
As a bonus, let’s also check out the Sawtooth channel from the VRC6 expansion. To begin with, a perfect Sawtooth wave is made of all the harmonics and each exhibits decreasing amplitudes (where `amplitude = 1 ÷ harmonic number` [[52]](https://www.copetti.org/writings/consoles/nes#bib:audio-sawtooth)).
This is quite a requirement for digital equipment and is naturally unaffordable for a game cartridge (which may not even need such perfection!). So, similarly to the APU’s triangle waves, the VRC6 sequences Sawtooth waves in 7 cycles (and thus produces similar step-ladder effects).
Consequently, the respective spectrogram appears very cluttered, as the VRC6’s approximation techniques fill the wave with extra harmonics in various places.
[« Previous](https://www.copetti.org/writings/consoles/nes#tab-5-4-sample) Next »
#### Conclusion
Well, it seems that the NES’ synthetic waveforms are nowhere near shaped as the theory dictates. Does this mean the APU is flawed? Not at all! The design of the APU ultimately gave this console its unique and identifiable sounds - these characteristics, whether intentional or not, made the spectrograms display unusual patterns.
As a side note, while perfect geometry may be visually appealing, our ears are surprisingly less receptive to waveforms with excellent edges! (you may start hearing popping noises).
Looking ahead, sound analysis using spectrograms will prove useful in other articles, whether for simple analysis or for comparing different systems. However, it is important to note that these graphs are not _the mother lode_ tool by all means, especially with sound samples that have been mixed with too many channels or instruments, which can complicate their decomposition. Nevertheless, they provide a solid foundation for any kind of objective study.
* * *
## Games
NES games are mainly written in the 6502 assembly language and reside in the **Program ROM** , while the game’s graphics (tiles) are stored in **Character memory**.
Furthermore, games were sold (or rented out) at retail stores **under the approval of Nintendo**.
### The alternative medium
Even though it was only released in Japan, I thought this would be a good opportunity to introduce a short-lived but peculiar add-on that, just like the mappers, brought in more capabilities to this console. This peripheral, called the **Famicom Disk System** (FDS), shipped in 1986 (~3 years after the Famicom). It resembled an external floppy drive and came bundled with an oddly shaped cartridge called the ‘RAM adapter’.
[![Image](https://www.copetti.org/images/consoles/nes/fds/drive.82f8f9c0064d1aff69e27d980adbee1909c9477f3f5456bfd859fd4b52eb44ba.png)](https://www.copetti.org/images/consoles/nes/fds/drive.82f8f9c0064d1aff69e27d980adbee1909c9477f3f5456bfd859fd4b52eb44ba.png)The drive [[53]](https://www.copetti.org/writings/consoles/nes#bib:photography-amos), where floppies are inserted (the photo shows a cardboard floppy inserted for protection). It either runs on six C batteries (1.5 V each) or a 3.6 W AC adapter.[![Image](https://www.copetti.org/images/consoles/nes/fds/ram.d2a1142d009657d0f70e73c8ee959db5b4784c55d9c9de3e609673ad6808193f.png)](https://www.copetti.org/images/consoles/nes/fds/ram.d2a1142d009657d0f70e73c8ee959db5b4784c55d9c9de3e609673ad6808193f.png)The RAM adapter [[54]](https://www.copetti.org/writings/consoles/nes#bib:photography-amos), fitted on the cartridge slot of the Famicom and connected to the drive via a cable.The two components that make up the Famicom Disk System (FDS).
The Famicom Disk System added the following functionality to the console:
  * A new medium of distribution for games called **Famicom Disk** [[55]](https://www.copetti.org/writings/consoles/nes#bib:games-fds). Based on the ‘Quick Disk’ by Mitsumi, it offers **~64 KB of data** per side and is re-writable.
  * An **extra audio channel** that uses [wavetable synthesis](https://www.copetti.org/writings/consoles/game-boy/#tab-3-2-wave) [[56]](https://www.copetti.org/writings/consoles/nes#bib:games-fds_audio).


[![Image](https://www.copetti.org/images/consoles/nes/fds/mounted.463081c651e753290930bdfaf74d75f21fc4d3f7e9e8e18c115503c56c3f12f8.png)](https://www.copetti.org/images/consoles/nes/fds/mounted.463081c651e753290930bdfaf74d75f21fc4d3f7e9e8e18c115503c56c3f12f8.png)FDS equipment mounted onto the Famicom [[57]](https://www.copetti.org/writings/consoles/nes#bib:photography-amos).
Unlike multi-chip cartridges, the floppy is a simple medium. Hence, all game data needs to be squashed inside, though it is organised with the use of a proprietary **file system**.
Nonetheless, the architecture of the Famicom/NES strictly enforces segregated Program and Character memory. The ‘RAM adapter’, which came with the box, addresses this by housing **32 KB of Program RAM** and **8 KB of Character RAM** to buffer the game data read from the floppy disk. In doing so, this setup enables the console to read data as if it were reading from a cartridge-based game.
To operate the drive, the RAM adapter embeds an additional 8 KB ROM to store a **BIOS** [[58]](https://www.copetti.org/writings/consoles/nes#bib:games-fds_bios). This program performs the following tasks:
  * Displays a splash animation.
  * Bootstraps the game from the floppy disk. Behind the scenes, the BIOS contains routines to copy the floppy’s contents to the appropriate memory chip, allowing the console to read them.
  * Provides I/O APIs for games to use, such as traversing the disk’s file system.


[![Image](https://www.copetti.org/images/consoles/nes/fds/floppies.4cef91964e9ee493b21a552bf3462f95d9bda3da671c22a21f120d508797ab13.jpg)](https://www.copetti.org/images/consoles/nes/fds/floppies.4cef91964e9ee493b21a552bf3462f95d9bda3da671c22a21f120d508797ab13.jpg)Example of two retail games for the FDS. The blue ‘flavour’ of the disc is dust proof. No support for video.The FDS splash animation, waiting for the user to… uhm… insert a game.
During that era, Nintendo deployed some ‘kiosks’ at retail stores, so users could bring their floppies and overwrite them with a new game at a reduced price.
Unfortunately, after a few years of lifespan, the Famicom Disk System was discontinued. Consequently, subsequent games reverted to the cartridge medium. On the bright side, new mappers were introduced with similar (or better) capabilities compared to the FDS’ functions.
* * *
## Anti-piracy and region lock
Nintendo was able to block unauthorised publishing by including a proprietary **lockout** chip called the **Checking Integrated Circuit** (CIC) [[59]](https://www.copetti.org/writings/consoles/nes#bib:anti_piracy-cic). It is located on the console’s motherboard and connected to the reset signal, making it difficult to remove.
The CIC runs **10NES** , an internal program that verifies the presence of another lockout chip in the game cartridge. If the verification fails, the console enters an infinite reset loop.
Both lockout chips are in constant communication during the console’s uptime. Nonetheless, this system can be bypassed by cutting one of the pins on the console’s lockout chip, which places it in an idle state. Alternatively, sending a -5V signal can halt it.
The CIC exists in response to the video game crash of 1983. Nintendo’s then-president, Hiroshi Yamauchi, decided that to ensure high-quality games, the company would take responsibility for approving every single title [[60]](https://www.copetti.org/writings/consoles/nes#bib:anti_piracy-vindicator).
You’ll notice that the Japanese model of the console, the Famicom, was released before the 1983 crash. That’s why neither game cartridges nor the console includes CIC circuitry [[61]](https://www.copetti.org/writings/consoles/nes#bib:anti_piracy-nocic). Instead, the pins are used for optional sound expansion.
* * *
## That’s all folks
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
- Any development cart out there (only if found at a reasonable price)
```

Alternatively, you can help out by [suggesting changes](https://github.com/flipacholas/Architecture-of-consoles) and/or [adding translations](https://github.com/flipacholas/Architecture-of-consoles).
* * *
## Copyright and permissions
This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). You may use it for your work at no cost, even for commercial purposes. But you have to respect the license and reference the article properly. Please take a look at the following guidelines and permissions:
Article information and referencing
For any referencing style, you can use the following information:
  * **Title of article** : NES / Famicom Architecture - A Practical Analysis
  * **Author** : Rodrigo Copetti
  * **URL** : <https://www.copetti.org/writings/consoles/nes/>
  * **Date of publication** : January 25, 2019
  * **Last modified** : May 24, 2025


For instance, to use with BibTeX:
```
@misc{copetti-nes,
    url = {https://www.copetti.org/writings/consoles/nes/},
    title = {NES / Famicom Architecture - A Practical Analysis},
    author = {Rodrigo Copetti},
    year = {2019}
}

```

or a IEEE style citation:
```
[1]R. Copetti, "NES / Famicom Architecture - A Practical Analysis", Copetti.org, 2019. [Online]. Available: https://www.copetti.org/writings/consoles/nes/. [Accessed: day- month- year].

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
### Anti-Piracy
  * Nesdev contributors, [CIC lockout chip](https://wiki.nesdev.org/w/index.php?title=CIC_lockout_chip). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:59)
  * thristian, [The japanese famicom didn’t have a CIC](https://news.ycombinator.com/item?id=1059686). Hackernews. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:61)
  * Jonathan Takiff, [Video games gain in japan, are due for assault on u.s.](https://news.google.com/newspapers?id=QBhcAAAAIBAJ&sjid=MlUNAAAAIBAJ&pg=2846,1271636). The Vindicator. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:60)


### Audio
  * Nesdev contributors, [APU](https://wiki.nesdev.org/w/index.php?title=APU). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:41)
  * Nesdev contributors, [APU pulse](https://www.nesdev.org/wiki/APU_Pulse). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:44)
  * Nesdev contributors, [APU noise](https://www.nesdev.org/wiki/APU_Noise) (accessed 08-January-2023). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:46)
  * Retro Game Audio, [NES audio: Review of the sound channels](https://retrogameaudio.tumblr.com/post/18843375536/nes-audio-review-of-the-sound-channels). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:43)
  * Jeffrey Stolet, [Complex periodic waveforms](https://pages.uoregon.edu/emi/10.php). University of Oregon. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:48)
  * Jeffrey Stolet, [Sawtooth waves](https://pages.uoregon.edu/emi/12.php). University of Oregon. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:52)
  * Jeffrey Stolet, [Harmonics](https://pages.uoregon.edu/emi/11.php). University of Oregon. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:49)
  * Jeffrey Stolet, [Triangle waves](https://pages.uoregon.edu/emi/13.php). University of Oregon. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:51)
  * Jeffrey Stolet, [Square and rectangle waves](https://pages.uoregon.edu/emi/14.php). University of Oregon. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:50)
  * Nesdev contributors, [APU triangle](https://www.nesdev.org/wiki/APU_Triangle). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:45)
  * Brad Taylor, [2A03 technical reference](https://retrogameaudio.tumblr.com/post/18843375536/nes-audio-review-of-the-sound-channels). 2004. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:47)


### CPU
  * Nesdev contributors, [CPU](https://wiki.nesdev.org/w/index.php?title=CPU). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:3)
  * VisualChips, [Visual6502 - 6502 binary-coded decimal (BCD mode)](http://visual6502.org/wiki/index.php?title=6502DecimalMode). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:13)
  * Nesdev Forums, [Difference between 6502 and 2A03 CPU core](https://forums.nesdev.com/viewtopic.php?f=9&t=9813). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:10)
  * Wikipedia contributors, [Semiconductor chip protection act of 1984](https://en.wikipedia.org/wiki/Semiconductor_Chip_Protection_Act_of_1984). Wikipedia, The Free Encyclopedia. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:14)
  * Radio Electronics, [Radio electronics magazine - december 1977 issue](https://worldradiohistory.com/Archive-Radio-Electronics/70s/1977/Radio-Electronics-1977-12.pdf). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:4)
  * Radio Electronics, [Radio electronics magazine - august 1981 issue](https://archive.org/details/radio_electronics_1981-08/page/n75/mode/2up). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:8)
  * Retrocomputing Beta, [How much did the 6502 and Z80 cost?](https://retrocomputing.stackexchange.com/questions/2760/how-much-did-the-6502-and-z80-cost). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:7)
  * Nikkei Trendi, [Nintendo "famicom" was born in this way](https://web.archive.org/web/20141017171734/http://trendy.nikkeibp.co.jp/article/special/20081002/1019378/). Archived, Japanese. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:11)
  * Travis Fahs, [The secret history of donkey kong](https://www.gamasutra.com/view/feature/134790/the_secret_history_of_donkey_kong.php?print=1). Gamasutra. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:12)
  * Tepples, [Sample RAM map](https://wiki.nesdev.org/w/index.php?title=Sample_RAM_map). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:15)
  * Nesdev contributors, [CPU memory map](https://wiki.nesdev.org/w/index.php?title=CPU_memory_map). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:18)
  * Nesdev contributors, [NROM](https://wiki.nesdev.org/w/index.php?title=NROM). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:20)
  * Nesdev contributors, [MMC3](https://wiki.nesdev.org/w/index.php?title=MMC3). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:22)
  * Babbage, [Motorola’s pioneering 8-bit 6800: Origins and architecture](https://thechipletter.substack.com/p/motorolas-pioneering-8-bit-6800-origins). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:9)
  * Babbage, [Leaving arizona](https://thechipletter.substack.com/p/leaving-arizona). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:6)


### Games
  * Nesdev contributors, [Family computer disk system](https://wiki.nesdev.org/w/index.php?title=Family_Computer_Disk_System). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:55)
  * Nesdev contributors, [FDS audio](https://wiki.nesdev.org/w/index.php?title=FDS_audio). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:56)
  * Nesdev contributors, [FDS BIOS](https://wiki.nesdev.org/w/index.php?title=FDS_BIOS). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:58)


### General
  * Nerdly Pleasures, [Official variations of the nintendo 8-bit NES/famicom console hardware](http://nerdlypleasures.blogspot.com/2017/06/official-variations-of-nintendo-8-bit.html). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:1)
  * Nesdev contributors, [Cartridge connector](https://wiki.nesdev.org/w/index.php?title=Cartridge_connector). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:42)


### Graphics
  * Nesdev contributors, [Overscan](https://wiki.nesdev.org/w/index.php?title=Overscan). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:23)
  * Nesdev contributors, [PPU nametables](http://wiki.nesdev.com/w/index.php/PPU_nametables). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:27)
  * Nesdev contributors, [PPU attribute tables](https://wiki.nesdev.com/w/index.php/PPU_attribute_tables). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:28)
  * Nesdev contributors, [PPU object attribute memory (OAM)](http://wiki.nesdev.com/w/index.php/PPU_OAM). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:40)
  * Nesdev contributors, [Color 0D games](https://wiki.nesdev.org/w/index.php?title=Color_$0D_games). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:39)
  * N3S, [N3S - how it works](http://web.archive.org/web/20190523120018/https://n3s.io/index.php?title=How_It_Works). Archived. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:36)
  * Retro Game Mechanics Explained, [The nintendo entertainment system’s loading seam](https://www.youtube.com/watch?v=wfrNnwJrujw). Youtube. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:35)
  * Tim Worthington, [RGB / s-video upgrade for nintendo NES](https://etim.net.au/nesrgb/). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:38)
  * Nesdev contributors, [PPU palettes](https://wiki.nesdev.org/w/index.php?title=PPU_palettes). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:37)
  * Rafael Bagmanov, [Writing NES emulator in rust - emulating PPU registers](https://bugzmanov.github.io/nes_ebook/chapter_6_1.html). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:24)
  * LilaQ, [Cartridge loading, pattern tables and ppu registers](https://emudev.de/nes-emulator/cartridge-loading-pattern-tables-and-ppu-registers/). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:25)
  * ChibiAkumas, [Hit me with your sprite 0 bit!](https://www.chibiakumas.com/6502/platform5.php). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:31)
  * dougfraker, [Sprite zero](https://nesdoug.com/2018/09/05/18-sprite-zero/). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:32)
  * Nesdev contributors, [PPU registers - PPUSTATUS](https://wiki.nesdev.org/w/index.php?title=PPU_registers#PPUSTATUS). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:30)
  * Nesdev contributors, [The frame and NMIs](https://wiki.nesdev.org/w/index.php?title=The_frame_and_NMIs). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:33)
  * Nesdev users, [Things in PPU that can change outside VBlank](https://forums.nesdev.org/viewtopic.php?p=80278). Nesdev Forums. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:34)


  * Nesdev contributors, [Open bus behavior](https://www.nesdev.org/wiki/Open_bus_behavior) (accessed 22-April-2025). Nesdev Wiki. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:17)


### Photography
  * Evan Amos, [The vanamo online game museum](https://commons.wikimedia.org/wiki/User:Evan-Amos). [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:57)
  * bootgod, [Super mario bros. 2 - NesCartDB](https://nescartdb.com/profile/view/268/super-mario-bros-2). NES Cart Database. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:21)
  * Kinopio, [Super mario bros. - NesCartDB](https://nescartdb.com/profile/view/2459/super-mario-bros). NES Cart Database. [↩︎](https://www.copetti.org/writings/consoles/nes#bibref:19)
  * Rodrigo Copetti (Me), [Diagrams and game screenshots](https://www.copetti.org/).


* * *
## Changelog
It’s always nice to keep a record of changes. For a complete report, you can check the [commit log](https://github.com/flipacholas/Architecture-of-consoles/commits/master/articles/nes.Rmd.md). Alternatively, here’s a simplified list:
```
### 2025-05-04
- Overall improvements to prepare for a book release.
- Extra history and description of the MOS 6502.
### 2024-08-07
- Expanded imagery after visiting Cambridge, UK.
### 2024-02-04
- Corrected OAM rotation explanation. See https://github.com/flipacholas/Architecture-of-consoles/issues/255 (thanks @cdmaczane).
### 2023-01-08
- Expanded audio channel information.
- Added extra study of the APU using spectrograms.
### 2021-12-26
- Improved Sprite zero mention.
### 2021-12-24
- Added Sprite zero mention.
### 2021-11-10
Super revamp:
- General improvements and corrections on each section.
- Added more info about mappers.
- Extended 'Graphics' section with new parts.
- New section about the Famicom Disk System.
- Better citation style.
### 2021-04-29
- General round of spelling and grammatical corrections. See https://github.com/flipacholas/Architecture-of-consoles/pull/30 (thanks @FormulatedEdits).
- Expanded Ricoh-MOS licensing mystery. See https://github.com/flipacholas/Architecture-of-consoles/issues/29 (thanks @djmips).
### 2020-08-23
- Added some historical context to the CPU section.
- Corrected assumptions about the lack of BCD, thanks @danweiss and @konrad.
- (Main diagram) Removed CPU connection to Character RAM, thanks @danweiss.
### 2020-06-13
- Added mention to OAM DMA.
### 2020-06-06
- Expanded BCD mode.
- Redesigned main diagram (the NES diagram was the first one for this site, since then the style evolved a lot!).
### 2019-09-17
- Added a quick introduction.
### 2019-04-06
- Corrected explanation about tile glitches.
### 2019-02-17
- Fixed Grammar.
- Replaced images and videos with better-quality ones.
### 2019-01-25
- Improved first draft with the help of @dpt
- Ready for publication
```

* * *
[« Architecture of Consoles](https://www.copetti.org/writings/consoles/) [Sega Master System Architecture »](https://www.copetti.org/writings/consoles/master-system/)
![Rodrigo Copetti](https://www.copetti.org/favicon/favicon.png)
### Rodrigo Copetti
I hope you have enjoyed this article! If you want to know more about the author [tap here](https://www.copetti.org/about/) and if you would like to support him [tap here](https://www.copetti.org/support/) instead
[Tweet ](https://twitter.com/intent/tweet?text=NES%20%2f%20Famicom%20Architecture%20%7c%20A%20Practical%20Analysis%20https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fnes%2f)[Share ](javascript:void\(0\))[Share ](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fnes%2f&title=NES%20%2f%20Famicom%20Architecture%20%7c%20A%20Practical%20Analysis&summary=An%20in-depth%20analysis%20that%20explains%20how%20this%20console%20works%20internally&source=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fnes%2f)[Share](https://reddit.com/submit?url=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fnes%2f&title=NES%20%2f%20Famicom%20Architecture%20%7c%20A%20Practical%20Analysis)
[Switch to classic edition](https://classic.copetti.org/writings/consoles/nes/)
Rodrigo Copetti © 2025 [](https://www.copetti.org/index.xml)
[About the website and its content](https://www.copetti.org/disclaimer/)
rsslinkedintwitterblueskygithub facebookreddit
