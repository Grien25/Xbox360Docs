# PlayStation Portable (PSP) Architecture | A Practical Analysis

**Source:** https://www.copetti.org/writings/consoles/playstation-portable

[Home](https://www.copetti.org/)
[Consoles](https://www.copetti.org/writings/consoles/)
[About](https://www.copetti.org/about/)
[Support](https://www.copetti.org/support/)
# PlayStation Portable (PSP) Architecture
## A practical analysis by Rodrigo Copetti
[](https://github.com/flipacholas/Architecture-of-consoles)[](https://crowdin.com/project/architecture-of-consoles)[](https://www.copetti.org/writings/consoles/materials/readings/)[](https://www.copetti.org/writings/consoles/playstation-portable)
If you use accessibility tools or old browsers, [switch to the ‘classic’ edition](https://classic.copetti.org/writings/consoles/playstation-portable/).
🇬🇧 - English 🇨🇳 - 简体字 👋 - Add translation
* * *
Book edition
[![eBook edition](https://www.copetti.org/images/consoles/_covers/en/playstation-portable_hu_142394a9d75d98d7.jpg)](https://www.copetti.org/writings/consoles/materials/book/)
This article is also published in many bookstores for the benefit of offline readers. The eBooks are DRM-free, while the printed editions compile multiple articles and feature original photography at full resolution.
You can find printed compilations [here](https://www.amazon.com/dp/B0F4P5RB25?binding=paperback), and individual eBooks at [Amazon Kindle](https://www.amazon.com/dp/B0B5VM3NHS), [Apple Books](https://books.apple.com/us/author/rodrigo-copetti/id1632545359?see-all=books), [Kobo](https://www.kobo.com/us/en/search?query=Architecture+of+Consoles%3a+A+Practical+Analysis&fcsearchfield=Series&seriesId=7e46f843-4aee-53b4-97c2-82782e951af5) and [other stores](https://www.copetti.org/writings/consoles/materials/book/). The proceeds support the improvement of current articles and the development of new ones.
For more information, please take a look at [here](https://www.copetti.org/writings/consoles/materials/book/).
* * *
Table of Contents
  1. [Supporting imagery](https://www.copetti.org/writings/consoles/playstation-portable#imagery)
  2. [A quick introduction](https://www.copetti.org/writings/consoles/playstation-portable#a-quick-introduction)
  3. [Main CPU](https://www.copetti.org/writings/consoles/playstation-portable#main-cpu)
    1. [MIPS after the turn of the century](https://www.copetti.org/writings/consoles/playstation-portable#mips-after-the-turn-of-the-century)
    2. [The new portable CPU](https://www.copetti.org/writings/consoles/playstation-portable#the-new-portable-cpu)
    3. [Coprocessors](https://www.copetti.org/writings/consoles/playstation-portable#coprocessors)
      1. [Focused memory management](https://www.copetti.org/writings/consoles/playstation-portable#focused-memory-management)
    4. [Memory available](https://www.copetti.org/writings/consoles/playstation-portable#memory-available)
    5. [Bus design](https://www.copetti.org/writings/consoles/playstation-portable#bus-design)
    6. [Tackling traffic congestion](https://www.copetti.org/writings/consoles/playstation-portable#tackling-traffic-congestion)
    7. [The end of the line](https://www.copetti.org/writings/consoles/playstation-portable#the-end-of-the-line)
  4. [Multimedia CPU](https://www.copetti.org/writings/consoles/playstation-portable#multimedia-cpu)
  5. [Graphics](https://www.copetti.org/writings/consoles/playstation-portable#graphics)
    1. [Display](https://www.copetti.org/writings/consoles/playstation-portable#display)
    2. [Introducing the Graphics Engine](https://www.copetti.org/writings/consoles/playstation-portable#introducing-the-graphics-engine)
    3. [Architecture of the Graphics Engine](https://www.copetti.org/writings/consoles/playstation-portable#architecture-of-the-graphics-engine)
    4. [Organising the content](https://www.copetti.org/writings/consoles/playstation-portable#organising-the-content)
    5. [Functionality](https://www.copetti.org/writings/consoles/playstation-portable#functionality)
      1. [Commands](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-1-commands)
      2. [Vector Processing](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-2-vector-processing)
      3. [Rasterisation](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-3-rasterisation)
      4. [Textures](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-4-textures)
      5. [Pixel Operations](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-5-pixel-operations)
      6. [Observations](https://www.copetti.org/writings/consoles/playstation-portable#observations)
    6. [Interactive models](https://www.copetti.org/writings/consoles/playstation-portable#interactive-models)
    7. [Video out](https://www.copetti.org/writings/consoles/playstation-portable#video-out)
  6. [Audio](https://www.copetti.org/writings/consoles/playstation-portable#audio)
    1. [Audio comparison](https://www.copetti.org/writings/consoles/playstation-portable#audio-comparison)
  7. [I/O](https://www.copetti.org/writings/consoles/playstation-portable#io)
    1. [Internal interfaces](https://www.copetti.org/writings/consoles/playstation-portable#internal-interfaces)
    2. [External interfaces](https://www.copetti.org/writings/consoles/playstation-portable#external-interfaces)
    3. [Commercial accessories](https://www.copetti.org/writings/consoles/playstation-portable#commercial-accessories)
    4. [Home console connectivity](https://www.copetti.org/writings/consoles/playstation-portable#home-console-connectivity)
  8. [Operating System](https://www.copetti.org/writings/consoles/playstation-portable#operating-system)
    1. [Architecture and design](https://www.copetti.org/writings/consoles/playstation-portable#architecture-and-design)
      1. [Modules](https://www.copetti.org/writings/consoles/playstation-portable#tab-2-1-modules)
      2. [Kernel/IPL](https://www.copetti.org/writings/consoles/playstation-portable#tab-2-2-kernelipl)
      3. [Other Parts](https://www.copetti.org/writings/consoles/playstation-portable#tab-2-3-other-parts)
    2. [Boot process](https://www.copetti.org/writings/consoles/playstation-portable#boot-process)
    3. [Visual Shell](https://www.copetti.org/writings/consoles/playstation-portable#visual-shell)
    4. [Updatability](https://www.copetti.org/writings/consoles/playstation-portable#updatability)
  9. [Games](https://www.copetti.org/writings/consoles/playstation-portable#games)
    1. [Development ecosystem](https://www.copetti.org/writings/consoles/playstation-portable#development-ecosystem)
    2. [Storage medium](https://www.copetti.org/writings/consoles/playstation-portable#storage-medium)
      1. [UMD Discs](https://www.copetti.org/writings/consoles/playstation-portable#tab-3-1-umd-discs)
      2. [Memory Stick Duo](https://www.copetti.org/writings/consoles/playstation-portable#tab-3-2-memory-stick-duo)
    3. [Network services](https://www.copetti.org/writings/consoles/playstation-portable#network-services)
      1. [PlayStation Network](https://www.copetti.org/writings/consoles/playstation-portable#tab-4-1-playstation-network)
      2. [PlayStation Store](https://www.copetti.org/writings/consoles/playstation-portable#tab-4-2-playstation-store)
      3. [Updatable content](https://www.copetti.org/writings/consoles/playstation-portable#tab-4-3-updatable-content)
  10. [Anti-Piracy and Homebrew](https://www.copetti.org/writings/consoles/playstation-portable#anti-piracy-and-homebrew)
    1. [Physical security](https://www.copetti.org/writings/consoles/playstation-portable#physical-security)
      1. [KIRK](https://www.copetti.org/writings/consoles/playstation-portable#tab-5-1-kirk)
      2. [Lepton](https://www.copetti.org/writings/consoles/playstation-portable#tab-5-2-lepton)
      3. [SPOCK](https://www.copetti.org/writings/consoles/playstation-portable#tab-5-3-spock)
    2. [Software security](https://www.copetti.org/writings/consoles/playstation-portable#software-security)
    3. [Defeat](https://www.copetti.org/writings/consoles/playstation-portable#defeat)
      1. [Early blunders](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-1-early-blunders)
      2. [Downgrading](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-2-downgrading)
      3. [Pandora](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-3-pandora)
      4. [CFW and beyond](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-4-cfw-and-beyond)
    4. [Homebrew encouragement](https://www.copetti.org/writings/consoles/playstation-portable#homebrew-encouragement)
  11. [That’s all folks](https://www.copetti.org/writings/consoles/playstation-portable#thats-all-folks)
  12. [Copyright and permissions](https://www.copetti.org/writings/consoles/playstation-portable#referencing)
  13. [Sources / Keep Reading](https://www.copetti.org/writings/consoles/playstation-portable#sources)
  14. [Contributing](https://www.copetti.org/writings/consoles/playstation-portable#contributing)
  15. [Changelog](https://www.copetti.org/writings/consoles/playstation-portable#changelog)


* * *
## Supporting imagery
  * [Model](https://www.copetti.org/writings/consoles/playstation-portable#cover-model)
  * [Motherboard](https://www.copetti.org/writings/consoles/playstation-portable#cover-motherboard)
  * [Diagram](https://www.copetti.org/writings/consoles/playstation-portable#cover-diagram)


### Model
  * [Original](https://www.copetti.org/writings/consoles/playstation-portable#cover-model-original)
  * [Slim](https://www.copetti.org/writings/consoles/playstation-portable#cover-model-slim)
  * [Slim & Lite](https://www.copetti.org/writings/consoles/playstation-portable#cover-model-slim--lite)
  * [Go](https://www.copetti.org/writings/consoles/playstation-portable#cover-model-go)

[![Original](https://www.copetti.org/images/consoles/psp/original.0efafae987c144250fb7f70ee83151321c0e5e892344eb35ace9a74ad640c18e.png)](https://www.copetti.org/images/consoles/psp/original.0efafae987c144250fb7f70ee83151321c0e5e892344eb35ace9a74ad640c18e.png)The original PSP (model 1000, a.k.a. 'Fat').  
Released on 12/12/2004 in Japan, 24/03/2005 in America and 01/09/2005 in Europe[![Slim](https://www.copetti.org/images/consoles/psp/slim.26eeff20144c4b7c986b8534d2c569603a3fbb856bd810b48a00336393de3ecf.png)](https://www.copetti.org/images/consoles/psp/slim.26eeff20144c4b7c986b8534d2c569603a3fbb856bd810b48a00336393de3ecf.png)The updated PSP (model 2000, a.k.a. 'Slim').  
Released on 05/09/2007 in Europe, 06/09/2007 in America and 20/09/2007 in Japan[![Slim & Lite](https://www.copetti.org/images/consoles/psp/slim-lite.48d6cb8d8d0c84d22eab394d67d9828adc6bcc643fc7643497370e10972540aa.png)](https://www.copetti.org/images/consoles/psp/slim-lite.48d6cb8d8d0c84d22eab394d67d9828adc6bcc643fc7643497370e10972540aa.png)The even-more-updated PSP (model 3000, a.k.a. 'Brite'), silver edition.  
Released on 14/10/2008 in America, 16/10/2008 in Japan and 17/10/2008 in Europe[![Go](https://www.copetti.org/images/consoles/psp/go.fd34fa7142e993a5c698f1926e4795ab94622f48bc8b3ad09584b8da9fd79bbc.png)](https://www.copetti.org/images/consoles/psp/go.fd34fa7142e993a5c698f1926e4795ab94622f48bc8b3ad09584b8da9fd79bbc.png)The redesigned PSP (model 'N1000', a.k.a 'Go').  
Released on 01/10/2009 in America and Europe, and on 01/11/2009 in Japan
### Motherboard
  * [Original](https://www.copetti.org/writings/consoles/playstation-portable#cover-motherboard-original)
  * [Marked](https://www.copetti.org/writings/consoles/playstation-portable#cover-motherboard-marked)

[![Motherboard](https://www.copetti.org/images/consoles/psp/motherboard.9c27e8cfff6b863445796eeb3f2a38b29780bda5fe4aed9cf0c916bd145479ba.png)](https://www.copetti.org/images/consoles/psp/motherboard.9c27e8cfff6b863445796eeb3f2a38b29780bda5fe4aed9cf0c916bd145479ba.png)Motherboard  
Such a tiny board... but you can do so much with it.  
Those zigzags you see between the CPU and memory attempt to correct the length of each bus so all of the signals arrive at the same time. This tells you how fast technology has become!  
After the 'Slim' model, Tachyon and 'NAND + SDRAM' became one.[![Motherboard](https://www.copetti.org/images/consoles/psp/motherboard_marked.1424fb70adcd5cc9b3e3d12763f72fac6e9465a8a1acc1a096a99c9d268227a6.png)](https://www.copetti.org/images/consoles/psp/motherboard_marked.1424fb70adcd5cc9b3e3d12763f72fac6e9465a8a1acc1a096a99c9d268227a6.png)Motherboard with important parts labelled
### Diagram
[![Diagram](https://www.copetti.org/images/consoles/psp/_diagrams/main.0a7c1c1f532346336f60abf62dc1366d4eb500aa88580fbec0229a25d78e2bf7.png)](https://www.copetti.org/images/consoles/psp/_diagrams/main.0a7c1c1f532346336f60abf62dc1366d4eb500aa88580fbec0229a25d78e2bf7.png)Main architecture diagram  
After the 'Slim' model, NAND and SDRAM size were doubled (to 64 MB each)
* * *
## A quick introduction
Released just one month after the [Nintendo DS](https://www.copetti.org/writings/consoles/nintendo-ds/), Sony’s PSP proved that ‘horizontal innovation’ is not the only way to succeed in the portable console market.
This article is dedicated to anyone who wants to understand, straight to the point, how the PSP operates. It’s not a short write-up, but I hope that at the end of the article, you will be able to grasp the building blocks of this console (its design rationale, choice of CPUs, GPU pipeline, security system and so forth).
* * *
## Main CPU
Similarly to Nintendo, Sony built an _extremely packed_ System-on-Chip (SoC) that houses most of the components we are going to discuss throughout this article. This includes the **main CPU** in charge of executing games and other programs (unlike the other CPUs, which we’ll talk about in due time). The SoC is called **Tachyon** , a name chosen by Sony themselves (after watching some _Star Trek_?).
[![Image](https://www.copetti.org/images/consoles/psp/tachyon.a7c25cb952548e37638dbaf3bf0dc7719c4e7824426d34c915caa5c5115a2677.jpg)](https://www.copetti.org/images/consoles/psp/tachyon.a7c25cb952548e37638dbaf3bf0dc7719c4e7824426d34c915caa5c5115a2677.jpg)The Tachyon chip on the original PSP model.
The main CPU is also an in-house design by Sony that [keeps up with the tradition](https://www.copetti.org/writings/consoles/playstation-2/#cpu) of using **MIPS** technology. Be as it may, it’s been four years since the release of the PlayStation 2, I wonder what’s the state of MIPS since then?
### MIPS after the turn of the century
I’m afraid the golden years of MIPS have been kept in the 90s and there aren’t any indicators that these will repeat anytime soon. Its parent company, SGI, lost dominance against affordable x86 workstations and was running out of cash. So, in 1999 it sold its majority stake in MIPS [[1]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-foremski). With this, MIPS became an independent company once again, however, the competition was more fierce than it was in the early days.
The company’s first decision was to acknowledge that MIPS CPUs couldn’t compute in the high-performance arena anymore. So, they shifted their focus to **low-power computing** , running head-to-head against [ARM](https://www.copetti.org/writings/consoles/game-boy-advance/#the-cambridge-miracle) and its [unprecedented popularity](https://www.copetti.org/writings/consoles/nintendo-ds/#arms-new-territories).
Consequently, MIPS revisited its fragmented CPU line and consolidated it with **three instruction sets** [[2]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-modern_mips):
  * **MIPS32** : An update of [MIPS II](https://www.copetti.org/writings/consoles/playstation/#the-offering) (the last 32-bit-only ISA) bringing functionality gathered from later architectures while keeping the 32-bit boundary.
  * **MIPS64** : The continuation of MIPS V, a [64-bit ISA](https://www.copetti.org/writings/consoles/nintendo-64/#cpu) and the last one before the revamp. The MIPS V has been a superset of all previous ISAs, just like its predecessors.
  * **microMIPS** : Available as ‘microMIPS32’ and ‘microMIPS64’, these are supersets of the MIPS32 and MIPS64, respectively, with an additional group of 16-bit instructions (à la [Thumb](https://www.copetti.org/writings/consoles/game-boy-advance/#tab-2-3-squeezing-performance)). microMIPS is not binary compatible with the other ISAs, however. Thus, it would require re-compilation of legacy codebases to run on microMIPS.


The big difference was that these would now be developed in conjunction, as opposed to MIPS dropping the previous architecture as soon as the next one arrived. New revisions would be denoted with the ‘Release x’ suffix, such as ‘MIPS32 Release 6’ or ‘MIPS32R6’ (coincidentally, the last revision to date).
Along with the ISAs, MIPS also started selling a new line of IP cores. For instance, the **MIPS32 4k** design implemented the **MIPS32 R2 ISA** , it came in different variants and offered plenty of customisations.
Back on topic, Sony presumably acquired a license of the MIPS32 4k and customised it by extending the ISA and bundling particular co-processors [[3]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-gcc_patch). The result is called **Allegrex** and runs at a variable speed, from **33 MHz to 333 MHz**.
### The new portable CPU
Allegrex is a complete 32-bit core offering [[4]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-hitmen) [[5]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-naked):
  * A **custom MIPS ISA** : mixes MIPS32R2 instructions with exclusive ones for **arithmetic operations** (multiplication, subtraction, min/max, bit-shifts) and **interrupt control**. These are called ‘Allegrex Extended Instructions’.
  * A **32-bit address bus** : this means that up to 4 GB of memory can be seen by this CPU.
  * **32 general-purpose registers** : all of them store 32-bit numbers; and two (the zero register and link register) are reserved for special uses. By now, this should come as no surprise.
  * A **7-stage pipeline** (one more than its [home sibling](https://www.copetti.org/writings/consoles/playstation-2/#a-special-order-for-sony)). [Here](https://www.copetti.org/writings/consoles/game-boy-advance/#tab-2-1-the-core) is a previous explanation of CPU pipelining if you’d like to know more.
  * **32 KB of L1 Cache** : of which 16 KB is for instructions and 16 KB for data.
  * A **cache write-back buffer** : the CPU can write over cache believing it has updated physical memory as well. Then, the cache takes care of updating memory when the buffer is full.
    * This design speeds up memory stores, but doesn’t work right away with multi-processor systems like the PSP. So, developers will have to take care of evicting the buffer when other components require those new values in memory.


This looks way more competitive than the [ARM9-based alternative](https://www.copetti.org/writings/consoles/nintendo-ds/#cpu), but it’s not over yet, as we still need to check the co-processors _cooperating_ next to the core.
### Coprocessors
As with any MIPS CPU, Allegrex has three coprocessor slots. Sony added three:
  * The **System Control Coprocessor** as ‘CP0’: a [necessary building block](https://www.copetti.org/writings/consoles/playstation/#tab-2-1-system-control-coprocessor) of any MIPS CPU. This particular component is what enables memory protection, cache coherency and interrupt control in the core itself [[6]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-mips_4k).
  * A **Floating Point Unit** (FPU) as ‘CP1’: accelerates arithmetic operations with 32-bit decimal numbers (following the IEEE 754 standard). It has **thirty-two 32-bit registers** and an **independent 8-stage pipeline** , thereby adding more parallelism to the main CPU.
  * A **Vector Floating Point Unit** (VFPU) as ‘CP2’: a coprocessor designed for **vector operations** , similar to a traditional SIMD processor. Compared to the FPU, it instead provides **128 32-bit registers** , relies on a proprietary instruction set and implements a variable-length pipeline. The VFPU operates up to 32-bit floating-point values, which can be grouped into a 4-component vector or **even a 4x4 matrix** (useful for different kinds of geometric operations without requiring to re-arrange the data).
    * Its efficiency comes from its 128-bit data bus connected to the rest of the system, offloading the main CPU’s transit.
    * Unlike the FPU, some behaviour of the VFPU deviates from the IEEE-754 standard.


In conclusion: Allegrex is incredibly fast. However, we still don’t know what can you do with it. After all, you can imagine this CPU as the conductor of an orchestra, and we haven’t checked out the performers yet.
#### Focused memory management
Let me talk for a moment about the memory system implemented in this system. Among other things, the System Control Coprocessor provides the functionality of a **Memory Protection Unit** or ‘MPU’ (not to be confused with an ‘MMU’), this maps the physical hardware onto the CPU’s memory space with some special quirks in between. Even though its _modus operandi_ can be seen as a bit primitive at first, we’ll see why it’s optimal for the needs of this console.
[![Image](https://www.copetti.org/images/consoles/psp/_diagrams/cpu/mmu.e203e0ea6a6aa12161940cb314ea9c88176dedc87bc67686ae73513c953a756e.png)](https://www.copetti.org/images/consoles/psp/_diagrams/cpu/mmu.e203e0ea6a6aa12161940cb314ea9c88176dedc87bc67686ae73513c953a756e.png)Memory addressing with the MPU.
A traditional Memory Management Unit or ‘MMU’ takes care of the CPU’s access to the components surrounding it. This implies that all the address lines of the CPU will be connected to the MMU; only the latter is connected to the rest of the system.
This is particularly advantageous for features like ‘virtual memory’ and ‘memory protection’. Well, to achieve virtual memory, an MMU must contain a component called ‘Translation Look-aside Buffer’ (TLB) to prevent performance degradation. Now, **Allegrex’s MMU lacks a TLB** , so it focuses on memory protection. This is why Allegrex’s MMU is instead called an MPU (Memory Protection Unit). An MPU is a cut-down version of an MMU without virtual memory. In any case, **memory protection gives the system the power to decide which memory locations a program can access**.
Thanks to this, Allegrex won’t have to deal with userland programs (i.e. games) accessing restricted locations (i.e. encryption keys). To accomplish the restriction itself, memory addresses are grouped into five segments with different privilege levels. Furthermore, Allegrex’s MPU contains three modes of operation: **User mode** , **Supervisor mode** and **Kernel mode**.
If a normal process (operating in user mode) wants to access a memory address found in a privileged location, the MPU will ask the operating system (through the use of ‘exceptions’) whether to grant permission to the process.
All in all, this allows Sony, the developer of the operating system, to implement a security system enforced by hardware.
### Memory available
So far we’ve analysed the PSP’s main CPU and its accelerators. Now let’s see the physical memory available in this system.
[![Image](https://www.copetti.org/images/consoles/psp/_diagrams/cpu/memory.fbca10a233424ccc4abe3d5a6d86f7613c9b86af7c53dde37ecdd5511ea0eae2.png)](https://www.copetti.org/images/consoles/psp/_diagrams/cpu/memory.fbca10a233424ccc4abe3d5a6d86f7613c9b86af7c53dde37ecdd5511ea0eae2.png)Memory layout from the main CPU perspective.
The PSP comes with two memory blocks accessible from the CPU:
  * **16 KB of SRAM** : this is what we called **Scratchpad** in [previous articles](https://www.copetti.org/writings/consoles/playstation/#cpu). It’s small but very fast RAM. It’s up to developers to make proper use of it, although unofficial documents called it ‘useless’.
  * **32 MB of DDR SDRAM** : it’s huge and many other components will make use of it, but since it’s not that close to the CPU, its access rate is slower. We’ll refer to it as ‘main memory’ across the article.
    * The ‘DDR’ initials mean ‘Double Data Rate’, which denotes an evolution from the traditional ‘SDRAM’, featuring a faster transfer protocol. The [original Xbox](https://www.copetti.org/writings/consoles/xbox/#memory-layout) used the same type.


### Bus design
You’ll soon find that the PSP accommodates lots of components with unique functionality. So, to organise them without repeating [previous mistakes](https://www.copetti.org/writings/consoles/nintendo-64/#tab-3-1-pipeline-stalls), engineers interconnected them using dedicated buses. Thus, only small groups of components, with similar applications, will share the same bus. Those buses talk to each other using dedicated arbiters (in the form of ‘memory controllers’ or Direct Memory Access (DMA)).
All of the buses found in Tachyon implement a well-known design called **Advanced High-performance Bus** (AHB), a solution built by Arm to tackle congestion on their chips and SoCs. If you are curious, AHBs are also used in the [Wii](https://www.copetti.org/writings/consoles/wii/#io).
[![Image](https://www.copetti.org/images/consoles/psp/_diagrams/cpu/buses.789eeb69ea63519a446c61d5178b75f1cd9af2162f635cfc537e0eba1caf7534.png)](https://www.copetti.org/images/consoles/psp/_diagrams/cpu/buses.789eeb69ea63519a446c61d5178b75f1cd9af2162f635cfc537e0eba1caf7534.png)Basic layout of the three main buses in this system.
Using the principles above, the following buses were constructed for the PSP:
  * The **System Bus** : connects the CPU, scratchpad and GPU. It’s 128 bits wide.
  * The **Media Engine bus** : connects another group of components (explained in the next section). It has the same properties as the System Bus.
  * The **Peripheral Bus** : connects I/O and storage-related components. It’s 32-bits wide.


All three buses connect to the DDR controller, which is where the main RAM is found.
### Tackling traffic congestion
Inside each bus, there will be multiple components working independently. They will store processed data in a shared space (such as the main RAM). Now, we don’t want the CPU to intervene whenever a module needs to read or write from memory. Traditionally, a DMA unit was placed in the bus to provide this facility, but a single DMA can only do so much. The PSP contains a significant number of components, and this will eventually lead to bottlenecks.
The solution is very simple: **bus mastering**. In a nutshell, each component will get its own DMA controller. This gives them the ability to become the ‘bus master’ and take control of the bus to access whatever location they want. To avoid contention (multiple ‘bus masters’ at the same time), the neighbouring components will acknowledge this event and wait until the operation completes.
### The end of the line
The RISC revolution spawned countless CPUs throughout the 80s-90s but only a handful lasted after the turn of the century. Just like I [concluded my analysis of the SuperH](https://www.copetti.org/writings/consoles/dreamcast/#end-of-the-line) in the [Dreamcast article](https://www.copetti.org/writings/consoles/dreamcast/), **the PlayStation Portable will be my last article of this series carrying a MIPS CPU**.
After many turnarounds, what’s left of MIPS is now a company designing **RISC-V** CPUs. In all fairness, this is an interesting strategy that provides the company with greater leverage to compete against ARM.
Looking back at my analyses, however, it’s hard to comprehend how such a talented company could’ve lost its market share. Admittedly, in the workstation market, it became clear that Intel’s x86, no matter the amount of criticism, won by making equipment affordable (thanks to its Pentium line, along with the ‘clones’) and attractive due to its (Windows-only) compatible software. Finally, the [P6 architecture](https://www.copetti.org/writings/consoles/xbox/#tab-1-4-cisc-or-risc) provided Intel with the scalability initially only enjoyed by RISC designs.
[![Image](https://www.copetti.org/images/consoles/psp/mips_interview.93f63f50948294794d1dba0572cc6d782ca86f2b4b07a1ae684f775076d04501.jpeg)](https://www.copetti.org/images/consoles/psp/mips_interview.93f63f50948294794d1dba0572cc6d782ca86f2b4b07a1ae684f775076d04501.jpeg)In 2011, the Computer History Museum (Mountain View, California) conducted an interesting interview with MIPS co-founders and former executives [[7]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-chm_mips), where they talked about MIPS’ beginnings, its impact on the industry and eventual reorganisation.
In the case of low-power computing, it was more difficult for me to understand the retreat, as MIPS and ARM shared similar business models (IP licensing). Luckily, a previous interview from the Computer History Museum in 2011 also brought up the same question, resulting in this answer:
> We made a mistake, we didn’t realise how important the cellphone market was. Early there was no money to be made (…) but ARM got it by [investing in it](https://www.copetti.org/writings/consoles/game-boy-advance/#tab-1-2-a-new-cpu-venture). It was a very smart move and it turned out to be incredible leverage point. We just looked at the gross margin and said “that’s not a great return! we’d be better off putting our attention elsewhere” but of course, it turned out cell phones became smartphones [and then] became a gigantic. [[8]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-chm_mips)
> – John Hennessy, co-founder of MIPS Computer Systems
Nevertheless, when it comes to this topic, I believe that, while we won’t see a new MIPS CPU, we’ll see the result of its former engineers transmitting its distinctive technology into new projects.
That being said, let’s take a look at the rest of the PSP components.
* * *
## Multimedia CPU
Up to this point, we’ve discussed the main CPU and the buses inside Tachyon, but there are still many features to be found in the SoC. In particular, there’s another block of modules designed for a specific application: **multimedia**. This group specialises in **audio and image processing** , including the combination of both (video processing), and it operates without consuming bandwidth from the main CPU group (the ‘system group’).
[![Image](https://www.copetti.org/images/consoles/psp/games/daxter.1cc7d9cf70d1b049affab4a0affcfbfebe71bbf9bb35f7e20a2adaf17b691d7e.jpg)](https://www.copetti.org/images/consoles/psp/games/daxter.1cc7d9cf70d1b049affab4a0affcfbfebe71bbf9bb35f7e20a2adaf17b691d7e.jpg)Daxter (2006).  
In-game cinematic rendered with this block.
That being said, the new block is called **Media Engine group** and it’s composed of the following components:
  * A second **Allegrex CPU** serving as the ‘controller’ of the Media Engine group. This is the same CPU found in the system group, but without the vector coprocessor [[9]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-marshall). The controller is responsible for receiving orders from the main CPU and managing the rest of the multimedia hardware that will work concurrently.
  * **2 MB of eDRAM** : multimedia encoding and/or decoding consumes a considerable amount of bandwidth, so to avoid stalling the other components, the Media Engine contains dedicated memory to process the data ‘in-house’ and publish the results once it’s necessary to do so.
    * ‘eDRAM’ is the same as DRAM but manufactured inside another chip.
  * An **MPEG-AVC** decoder: a hardware decoder that does only one thing, and fast. That is, swallow **H.264 video stream** [[10]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-ppsspp) and spit out data that the audio and graphics endpoint understand.
  * A **Virtual Mobile Engine** or ‘VME’: this is _some sort_ of programmable Digital Signal Processor (DSP). The controller programs it and then starts feeding in the data. Afterwards, like the AVC, the VME stores the processed chunk in local memory.
    * This is a very obscure component; only Sony seems to know the ins and outs of it (including how to program it). To this day, it’s still a mystery.
    * From what it seems to be Sony’s leaked slides [[11]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-specs), the VME seems to have local memory and a DMA controller. It’s also known as the ‘Dynamic Reconfigurable Engine’.


Needless to say, the Media Engine is not directly operable from the developer’s side (Sony hides all of it through a thick API). The official Software Development Kit (SDK) includes libraries like ‘libmpeg’ or ‘libmp3’ which already implement complete applications optimised for this engine.
* * *
## Graphics
To begin with, let’s go over the physical screen of this console, which is where the user can appreciate everything that will be discussed in this section.
### Display
The PSP carries a **4.3” TFT LCD screen**. It has a resolution of **480x272 pixels** (for reference, that’s ~2.6 times the pixels of one screen of the Nintendo DS) and can display up to 16,777,216 colours. Thus, it’s got a 24-bit colour depth (the so-called ‘true color’ scale).
The aspect ratio is _almost_ 16:9, a format which during that time was increasingly becoming standard on home TVs. Notice that a wider range of view is also an opportunity for game designers to improve the experience (especially in the first-person shooting genre).
### Introducing the Graphics Engine
Now it’s time to talk about the component in charge of producing pixels, the **Graphics Engine** (GE). The engine is found within the ‘system group’, so you may see it as a ‘group within a group’. Below you can see some of the results it achieved:
  * [KH](https://www.copetti.org/writings/consoles/playstation-portable#nestedtab-1-1-kh)
  * [Spider-Man](https://www.copetti.org/writings/consoles/playstation-portable#nestedtab-1-2-spider-man)
  * [GTA](https://www.copetti.org/writings/consoles/playstation-portable#nestedtab-1-3-gta)
  * [Sims 2](https://www.copetti.org/writings/consoles/playstation-portable#nestedtab-1-4-sims-2)
  * [OutRun](https://www.copetti.org/writings/consoles/playstation-portable#nestedtab-1-5-outrun)
  * [Loco](https://www.copetti.org/writings/consoles/playstation-portable#nestedtab-1-6-loco)

[![Image](https://www.copetti.org/images/consoles/psp/games/kh.10599c6dfb79822922581db1ea8211778d23e64e6564fc887726861993264ee5.jpg)](https://www.copetti.org/images/consoles/psp/games/kh.10599c6dfb79822922581db1ea8211778d23e64e6564fc887726861993264ee5.jpg)Kingdom Hearts Birth by Sleep (2010).[![Image](https://www.copetti.org/images/consoles/psp/games/spider.cca57f790e5faa6a2bc8f30a87106c5c0a6f041d48f189b5f6209adf28de22cc.jpg)](https://www.copetti.org/images/consoles/psp/games/spider.cca57f790e5faa6a2bc8f30a87106c5c0a6f041d48f189b5f6209adf28de22cc.jpg)Spider-Man 3 (2007).[![Image](https://www.copetti.org/images/consoles/psp/games/gta.f09af3e7d2ad1f33bc75758cde9008ed3b01a7582c0cc626e6ca8d895c40b9cf.jpg)](https://www.copetti.org/images/consoles/psp/games/gta.f09af3e7d2ad1f33bc75758cde9008ed3b01a7582c0cc626e6ca8d895c40b9cf.jpg)Grand Theft Auto: Vice City Stories (2006).[![Image](https://www.copetti.org/images/consoles/psp/games/sims2.3dccdf3ef409b5c664150290d16272585046aa5237d98cc639dbebb80e78e970.jpg)](https://www.copetti.org/images/consoles/psp/games/sims2.3dccdf3ef409b5c664150290d16272585046aa5237d98cc639dbebb80e78e970.jpg)The Sims 2 (2005)[![Image](https://www.copetti.org/images/consoles/psp/games/outrun.ecbec05951adb5f9bac3e5c0d7e9c4f094ad7dd8c9d486752b764e82f613ac01.jpg)](https://www.copetti.org/images/consoles/psp/games/outrun.ecbec05951adb5f9bac3e5c0d7e9c4f094ad7dd8c9d486752b764e82f613ac01.jpg)OutRun 2006: Coast 2 Coast (2006)[![Image](https://www.copetti.org/images/consoles/psp/games/loco.d60fff92ce9a2aa66fdaa77c519e0dcf8e5fa05d8c571174773e91de5e4760c4.jpg)](https://www.copetti.org/images/consoles/psp/games/loco.d60fff92ce9a2aa66fdaa77c519e0dcf8e5fa05d8c571174773e91de5e4760c4.jpg)LocoRoco (2006)Example of PSP games. All rendered at their maximum resolution (480x272 pixels).
The GE draws 3D graphics (polygons) with many features applied (texture mapping, lighting and so much more), which you’ll see in a bit.
### Architecture of the Graphics Engine
The GE subsystem has lots of interesting quirks to mention, so this will be a very complex section. But fear not! I’ll try to go step-by-step to avoid any confusion.
First things first – the GE is made of three components:
  * The **graphics core** : where the actual graphics functionality happens.
  * The **eDRAM controller** : mediates access between eDRAM memory and the core.
  * The **bus matrix** : works as a ‘bus arbiter’ between the System Bus and the internals of the GE (remember the GE is found within the system group).
    * In reality, this component is a mesh of wires with some logic, but for the sake of explaining, it’s simpler to mask with a black box.


The reason for this design is that both main CPU and the graphics core can access those 2 MB of eDRAM. So, to prevent congestion, the traffic inside the GE goes through another Advanced High-performance Bus called **local bus** (‘local’ from the perspective of the GE). This allows the graphics core to perform its functions without depending on the System Bus to move data around (and consequently stalling the rest of the system).
[![Image](https://www.copetti.org/images/consoles/psp/_diagrams/ge_arch.d963ccf084e42ace788d5bee3d16e6ad4391891b473f9f05a0f442dcae0df645.png)](https://www.copetti.org/images/consoles/psp/_diagrams/ge_arch.d963ccf084e42ace788d5bee3d16e6ad4391891b473f9f05a0f442dcae0df645.png)Architecture of the Graphics Engine.
The local bus is as wide as the System Bus (128 bits), but if that wasn’t enough, the graphics core has a direct line to eDRAM using a 512-bit bus (made of two unidirectional 256-bit buses). You’ll see why it will be needed in the following section.
What about how the CPU and GE communicate with each other? As I said before, both CPU and graphics core can read from eDRAM. Additionally, the graphics core can access the System Bus to fetch data from any other component (including the main RAM). So, all of that just doesn’t happen magically.
In a nutshell, two **bus matrix** blocks re-wire the connection between the local bus and the System Bus. Whenever there’s a component that wants to access an ‘alien’ bus, the bus matrices configure the communication so that one unit becomes master of the two buses and no other overlaps, this persists until the designated unit finishes transferring memory.
This behaviour reminds me of the commonly known technique called **bus mastering** , where the leading component is the ‘bus master’ and has complete control of the bus, and the rest are ‘slaves’ waiting for commands. However, I’m not sure which protocol/standard Sony’s engineers were trying to replicate. Based on my understanding, I think it may be somewhat similar to I²C, a protocol used for serial communications (particularly useful with embedded systems) that also performs bus mastering.
### Organising the content
Now that we’ve seen what components we’ve got and how they interact with each other, let’s find out what information related to graphics we can place in memory.
There are three memory locations from which the GE will end up pulling from or filling:
  * **2 MB eDRAM** : the aforementioned eDRAM. It’s used to store the frame-buffer, [z-buffer](https://www.copetti.org/writings/consoles/nintendo-64/#modern-visible-surface-determination) and texture buffer. Its contents are directly written by the GE. This memory space is also called ‘local memory’.
    * The CPU can access this memory if needed, although its speed is not ideal.
  * **32 MB DDR SDRAM** : this is the working area of the CPU for building display lists, vertex data, texture data and CLUTs (Colour lookup tables). In the context of graphics, this bloc is called ‘host memory’.
  * **16 KB SRAM** : the scratchpad memory is also accessible by both CPU and GE.


### Functionality
Like its [home sibling](https://www.copetti.org/writings/consoles/playstation-2/#graphics), the PSP’s graphics system focuses on **rasterisation**. However, the PSP’s VRAM is half the size of the PS2’s, and its bus is not as fast. To compensate, the PSP’s Graphics Engine features a vector processor!
[![Image](https://www.copetti.org/images/consoles/psp/_diagrams/gpu/pipeline.9225d35b3f8a57b90212d0ad3f3c02154c12d50b003e58613b1106f9d138eaa0.png)](https://www.copetti.org/images/consoles/psp/_diagrams/gpu/pipeline.9225d35b3f8a57b90212d0ad3f3c02154c12d50b003e58613b1106f9d138eaa0.png)Pipeline design of the Graphics Engine.  
I’ve skipped the interfaces since it’s becoming too convoluted.
The graphics pipeline is very similar to that of the PS2, with the addition of the vector processing stage. The graphics core is divided into two areas: the **surface engine** , which deals with vector processing, and the **rendering engine** which, as its name indicates, performs rasterisation and effects.
Although its features have been explained in the past [[12]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-programming), the details of the graphics pipeline itself have not. The truth is, programmers don’t depend on that information to build their games. However, for the sake of this analysis, I’ve deduced a model myself.
On another note, I’ve decided to make it a bit more technical than previous articles. I thought this would be a good opportunity to learn new concepts and have a wider vision of computing graphics. Having said that, I strongly recommend reading about the [PS1](https://www.copetti.org/writings/consoles/playstation/#graphics) and [PS2](https://www.copetti.org/writings/consoles/playstation-2/#graphics) graphics systems before continuing.
  * [Commands](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-1-commands)
  * [Vector Processing](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-2-vector-processing)
  * [Rasterisation](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-3-rasterisation)
  * [Textures](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-4-textures)
  * [Pixel Operations](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-5-pixel-operations)


#### Commands
[![Image](https://www.copetti.org/images/consoles/psp/_diagrams/gpu/commands.3acff49963e1afe64ccf3778448e685b2efd8a82276eb947ce90b1ac7204d787.png)](https://www.copetti.org/images/consoles/psp/_diagrams/gpu/commands.3acff49963e1afe64ccf3778448e685b2efd8a82276eb947ce90b1ac7204d787.png)Command stage.
The Graphics Engine is controlled using traditional ‘display lists’ stored in main memory. The CPU builds them and the GPU reads them (using Direct Memory Access). Display lists basically tell the GPU what, how and where to draw. In the case of the PSP, display lists are not limited to rendering tasks – they can also include vector transformations.
The strategy implemented to process lists is critical to ensure that the CPU and GPU work concurrently and don’t stall each other. Remember, we want the GPU to accelerate operations, not to be a burden. Hence, the CPU and GPU support **deferred rendering** , a technique that allows the CPU to build the next set of display lists while the GPU is processing a previous one. The GE is configured by specifying where in memory the display list starts (base address) and where it stops (stall address). As a result, there are two ways of allocating a list:
  * **Double buffered** : there are two separate display lists areas. One is being transferred to the GPU, the other is being filled by the CPU. When both processors finish, they swap places.
  * **Store controlled** : the CPU fills the same list the DMA unit is transferring to the CPU, but the CPU is some entries ahead to avoid overlapping. This uses less memory but it’s susceptible to stalls if the GPU catches up.


Furthermore, Sony stated that the GPU’s DMA unit is not just a ‘dumb memory copier’ – it can also understand the data transferred [[13]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-programming). Thus, display lists can include **commands** such as `jump` and `return` to tell the DMA to branch out and get data from somewhere else. This saves the CPU from embedding large resources (models, textures, etc.) in the display lists (which would effectively duplicate data in memory) and reduces bandwidth consumption. This system was inherited from the PS2.
Finally, the DMA can also interpret **bounding box data** : combined with information stored in the GE, the DMA will skip drawing commands that aren’t within the display area. It’s also possible to declare bounding boxes inside other bounding boxes, but let’s leave that topic for another day!
« Previous [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-2-vector-processing)
#### Vector Processing
[![Image](https://www.copetti.org/images/consoles/psp/_diagrams/gpu/vector.513aba36c930069c928522d3043d4e4507b24a90d6d99859c3a0f1cbdd58ba3d.png)](https://www.copetti.org/images/consoles/psp/_diagrams/gpu/vector.513aba36c930069c928522d3043d4e4507b24a90d6d99859c3a0f1cbdd58ba3d.png)Vector Processing stage.
The Graphics Engine debuts the ability to perform operations over vectors, which helps to offload a lot of work from the CPU. Sony built this unit to accelerate common tasks previously carried out by the PS2’s VPUs using microcode [[14]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-programming). While the GE is not as flexible as a VPU (the GE is a fixed-function unit), it does simplify a lot of coding (considering microcode had a considerable weight on the learning curve). The GE’s vector processor is called **surface engine**.
The surface engine undertakes **three types of task**. The first is the operation of **parametric surfaces** [[15]](https://www.copetti.org/writings/consoles/playstation-portable#bib:graphics-pspdkgu). Remember the [‘Infinite Worlds’](https://www.copetti.org/writings/consoles/playstation-2/#infinite-worlds) section? Well, Sony explained that, while the PS2 was indeed capable of this, in the end just a few games bothered. It’s possible that polygon performance, along with difficulty in design and implementation, were the main factors.
To tackle this, the surface engine implements two parametric curves:
  * **Bézier** : a relatively fast function but its parameters change the global shape. Additionally, it suffers from ‘continuity issues’ which manifest as cracks on surfaces (discouraging its use with animations). It’s often used for landscape generation.
  * **B-spline** : requires more computations but fixes continuity issues and provides localised control. Character modelling and animation are potential candidates.


Both support **levels of detail** , which means that developers can set an arbitrary value to alter the level of subdivision (impacting the quality of the resulting model).
The second task is called **vertex blending** , a technique used for **animations**. The surface engine provides two types:
  * **Skinning** (a.k.a skeleton animation): movement relies on a structure of ‘joints’ attached to the character model. It’s often applied for normal animation (walking, jumping, etc.).
  * **Morphing** : uses multiple instances of a model and averages them to get a ‘transition effect’ (using linear interpolation). It’s normally used for artificial animation (i.e. facial movement) and special effects. It comes with larger memory consumption and a steeper learning curve.


It’s important to denote that the CPU may still need to compute animations to process game logic (e.g. collision detection), so the CPU can’t offload all the work.
Finally, the surface engine provides **scissoring** (discarding vertices outside the viewport/rectangular area) as well.
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-1-commands) [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-3-rasterisation)
#### Rasterisation
[![Image](https://www.copetti.org/images/consoles/psp/_diagrams/gpu/rendering.68908e4f59bd7d4c3d463ddc2d8f31ca2c1bb1a45da713d5004924dde15ddb69.png)](https://www.copetti.org/images/consoles/psp/_diagrams/gpu/rendering.68908e4f59bd7d4c3d463ddc2d8f31ca2c1bb1a45da713d5004924dde15ddb69.png)Rasterising stage.
The next stage of graphics generation takes place in the **rendering engine** (skipping the command processor). In here, vector data is transformed into pixels, which is pretty much in pace with any other GPU in the market.
The engine draws many types of primitives, including points, lines, line strips, triangles, triangle strips, triangle fans and, finally, sprites (made of 2D rectangles). It also contains a unit called ‘digital differential analyser’ that will be used for interpolating values during rasterisation and texture mapping.
Developers can supply a projection matrix to apply **perspective transformation**. This sends their 3D world to a 2D space (so you can see it on the screen), using the virtual camera as a model.
Sony didn’t provide much information about how its rasteriser works in particular, so it’s not well-known how many pixels are processed per cycle, for instance. Modern features, like sub-pixel precision, are assumed to be implemented (otherwise, users would’ve been able to [spot its absence](https://www.copetti.org/writings/consoles/playstation/#tab-4-1-distorted-modelstextures) right away).
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-2-vector-processing) [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-4-textures)
#### Textures
[![Image](https://www.copetti.org/images/consoles/psp/_diagrams/gpu/textures.3059f03139a77530cd12b9a8d7f8704a0c7c8e0dab127b57a920a4f9b471e93d.png)](https://www.copetti.org/images/consoles/psp/_diagrams/gpu/textures.3059f03139a77530cd12b9a8d7f8704a0c7c8e0dab127b57a920a4f9b471e93d.png)Texture mapping stage.
This may be the topic of most interest for some. Polygons (now mere pixels) can be painted with textures. At this stage, texture maps are fetched from memory and processed with many functions. This process is called **texture mapping**.
The rendering engine has three **mapping modes** or, in other words, three ways of processing texture maps:
  * **UV mapping** : every coordinate of the model is mapped to a coordinate of the texture.
  * **Projective mapping** : in a nutshell, it simulates a physical projector shining the texture map over a surface.
  * **Shade mapping** : casts up to four lights (ambient, directional, point or spot) on the model. This is useful when blending the result with another map (you’ll see more in the next section).
    * If programmers supply a texture map instead of a solid colour, you get a ‘fish eye’ effect (useful for reflections, a.k.a. **environmental mapping**).
    * This mode also permits [toon shading](https://www.copetti.org/writings/consoles/gamecube/#creativity).


Textures may use **Colour Lookup Tables** or ‘CLUTs’. Furthermore, this engine applies **perspective correction** and **bilinear or trilinear filtering** for interpolation.
On another topic, there’s **8 KB of texture cache** found in the GE to save bandwidth. It uses the ‘least recently used’ method for space management.
Finally, while this pipeline is not programmable, developers can send extra colours to be blended with textures. There’s also colour doubling (which doubles the RGB value of colours), colour addition (combines a primary colour with a secondary colour) and **fogging** (haze over distant polygons).
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-3-rasterisation) [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-5-pixel-operations)
#### Pixel Operations
[![Image](https://www.copetti.org/images/consoles/psp/_diagrams/gpu/operation.4d848a1cf7e348a24ab0f161f18486184e8de451b7be52e9f0c927946247ea2d.png)](https://www.copetti.org/images/consoles/psp/_diagrams/gpu/operation.4d848a1cf7e348a24ab0f161f18486184e8de451b7be52e9f0c927946247ea2d.png)Pixel operation stage.
We’re reaching the end of the pipeline. The initial geometry has been transformed into pixels and these are now rich-coloured, so it’s time to decide what to do with them.
Some pixels may correspond to geometry that is not needed for this frame (it might be occluded, masked, etc.). To filter that out, the GE can perform the following tests:
  * **Scissoring** : discards polygons away from an arbitrary area.
  * **Depth range** : discards too distant or too near polygons (developers set the reference values).
  * **Colour** : discards pixels equal or not equal to an RGB value.
  * **Alpha** : compares the pixel’s alpha value to a reference value.
  * **Stencil** : similar to alpha, but relies on the stencil value.
  * **Depth test** : late [Z-buffering](https://www.copetti.org/writings/consoles/nintendo-64/#modern-visible-surface-determination).


Afterwards, pixels will also travel through these optional blocks for further effects:
  * **Alpha blending** : combines non-opaque pixels with the ones in the frame-buffer using different arithmetic operators.
  * **Dithering** : softens colour changes.
  * **Colour clamping** : aligns RGB values to fit in the frame-buffer format.
  * **Logical operation** : decides how to merge the new frame with the existing frame-buffer using logical operators (`AND`, `OR` and many more).
  * **Masking** : as the name indicates, it masks the z-buffer or frame-buffer.


Complex functions like **antialiasing** are the result of a strategic combination of the above. Finally, the outputted pixel is written to the frame-buffer, which in turn is sent for display.
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-1-4-textures) Next »
#### Observations
As evidenced, the PSP inherits various features from the PS2. The difference, however, is that functionality is now hardwired in the silicon, as opposed to offering many general-purpose programmable units (which require manual work to set them up). I presume this was done for two reasons: to use fewer transistors (so it fits in Tachyon and the board remains ‘portable’) and to facilitate porting PS2 codebases to the new console.
### Interactive models
To show how this system impacted model design and to help compare it to the [PS2](https://www.copetti.org/writings/consoles/playstation-2/#better-models) and [Nintendo DS](https://www.copetti.org/writings/consoles/nintendo-ds/#interactive-models), here are two examples of models designed for the PSP. Don’t forget the viewer is interactive!
Wireframe | Surface | Textured  
---|---|---  
![3D model](https://www.copetti.org/images/consoles/models/snake_psp.00979906c7a24be31de879b4b0afdd3c5362f693c93465209e48109dc00921d0.png)  
Tap to enable interaction  
Metal Gear Solid: Portable Ops Plus (2006).  
1,383 triangles. Wireframe | Surface | Textured  
---|---|---  
![3D model](https://www.copetti.org/images/consoles/models/daxter_psp.ea4d9b8af9d0a7ec7b14e383a802fec15043a9bed16efcce1c018dce8410cc81.png)  
Tap to enable interaction  
Daxter (2006).  
1,374 triangles.
### Video out
The first model of this console (1000) has a proprietary video port called **remote port** at the bottom-left corner (next to the audio jack).
[![Image](https://www.copetti.org/images/consoles/psp/io/bottom.f2a565a2ac74c97efc587423833b9ff3c35f4e648faaa767e90e18c1401e5440.jpg)](https://www.copetti.org/images/consoles/psp/io/bottom.f2a565a2ac74c97efc587423833b9ff3c35f4e648faaa767e90e18c1401e5440.jpg)Bottom-right corner of the PSP (3000 model) showing the proprietary ‘Video Out’.
The remote port uses the RS-232 protocol [[16]](https://www.copetti.org/writings/consoles/playstation-portable#bib:io-nil), an old standard for transferring data in serial. Though the specification wasn’t publicly available to developers (let alone documented), a couple of audio headsets with control buttons appeared on the market. They apparently use the serial port to send commands (play, pause, etc.) to the console.
In later models (2000 and 3000), the remote port was expanded with an extra YCbCr pinout. Sony shipped three **video cables** (component, S-Video and composite) that rely on this interface to enable users to see the contents of the PSP screen on the TV.
The video cable will send a frame with a resolution of **720x480 pixels (in NTSC) or 720x576 pixels (in PAL)** , in progressive or interlaced mode (the latter option is only available on the 3000 model). As the PSP’s resolution is 480x272 pixels, games will show **black bars** to correct the aspect ratio. However, the bars won’t show when the console is running the ‘XMB’ visual shell, which natively supports adjusting its resolution according to the video cable.
* * *
## Audio
(Please note that there isn’t space to define and explain every term used in this section. Where a term is uncommon, you can usually find a more comprehensive explanation in other articles from this series. I’ve put links where I can.)
In this section we tend to encounter a [PSG](https://www.copetti.org/writings/consoles/master-system/#audio), [sequencer](https://www.copetti.org/writings/consoles/nintendo-64/#audio) or a _large_ [mixer](https://www.copetti.org/writings/consoles/nintendo-ds/#audio). This is because, at the end of the day, dedicated audio hardware is meant to offload audio operations from the CPU. Although if this hardware turns out to be ‘weak’, it degrades the sound capabilities of the console.
Now, what we consider ‘sound hardware’ in the PSP is very bare-bones: only **two PCM channels and a stereo mixer**. The maximum sampling rate and resolution are **48 kHz** and **16-bit** , respectively.
I don’t see any of the accelerators I mentioned in the first paragraph. So, does this imply that the sound will be as limited as [other](https://www.copetti.org/writings/consoles/nintendo-64/#secrets-and-limitations-1) [cases](https://www.copetti.org/writings/consoles/game-boy-advance/#audio) showed? No! Because the hardware of the PSP enables to compensate it with more software.
You see, while there isn’t a large amount of sound-related circuitry, Sony supplied a lot of general-purpose components. These can help with audio decoding, streaming and mixing. I’m talking about the **Media Engine**.
That block is very good at signal processing, but it needs to be programmed. So, Sony wrote the following software for the Media Engine to complement the two PCM channels (we’ll call these the ‘endpoint’) [[17]](https://www.copetti.org/writings/consoles/playstation-portable#bib:audio-sad) [[18]](https://www.copetti.org/writings/consoles/playstation-portable#bib:audio-sas):
  * **Sound driver** : talks to the endpoint and performs memory transfers using DMA.
  * **Software audio synthesizer** : as the name indicates, it generates the signals to be sent to the endpoint.
    * This synthesizer supports 32 channels, using the **PCM** , **ADPCM** or **ATRAC3** formats [[19]](https://www.copetti.org/writings/consoles/playstation-portable#bib:io-edepot).
    * Provides **digital reverb** , **pitch control** and **ADSR envelope**.


Games don’t have access to these modules directly. Instead, they call many libraries included in the official SDK. Some libraries are designed to operate raw signals while others are optimised for particular applications. Examples include:
  * **MP3 and AAC decoding**.
  * **MIDI sequencing**.
  * **VoIP audio decoding** (G729 and u-law).
    * The operating system of the PSP bundled a variant of the ‘Skype’ app, if you wonder what uses VoIP could have here.


### Audio comparison
Let’s put all this into practice by taking a look at how games reproduced their sound. I wrote this special player that allows you to swap between consoles (to enable side-by-side comparisons):
Nintendo DS | PSP  
---|---  
No support for audio. No support for audio.  
Tap to enable interaction  
**Nintendo DS:** Final Fantasy IV (2007).  
**PSP:** Final Fantasy IV - The Complete Collection (2011). PlayStation 2 | PSP  
---|---  
No support for audio. No support for audio.  
Tap to enable interaction  
**PlayStation 2:** Kingdom Hearts 2 (2005).  
**PSP:** Kingdom Hearts Birth by Sleep (2010).
In the first example, the Nintendo DS game sequences its music on the fly, while the PSP one decodes ATRAC3. As you can hear, having no dedicated sound hardware _per se_ doesn’t imply poor sound quality. In fact, one could argue the opposite, as the Media Engine provided more features than the sound chips of most previous portable consoles ever did.
The second example is much trickier to quantify. I placed a PS2 tune for comparison, but I had to boost the PS2 one a bit (I presume PSP soundtracks are louder to compensate for the smaller speaker and the proximity to the user). Also, bear in mind that the arrangements are slightly different between platforms. It’s possibly just a creative change since the PSP game was released five years after the PS2 one. Overall, the PSP doesn’t show deterioration (considering that the [PS2’s SPU2](https://www.copetti.org/writings/consoles/playstation-2/#audio) is very powerful and flexible).
* * *
## I/O
The PSP has plenty of connections and sensors. However, this section will be a good opportunity to introduce some chipsets that haven’t been mentioned yet. These play a big part in handling the circuitry that detects the player’s input.
### Internal interfaces
Most of the I/O available is linked in the **Peripheral Bus**. It’s only 32 bits wide, which is enough to transfer simple information at a normal pace. It has access to the main RAM as well.
The D-pad, joystick and buttons are handled by a unique chip referred to as **‘System Control’ or SysCon**. This is a common codename in Sony’s hardware and it deals with interfacing many internal components – in this case, only the physical buttons.
### External interfaces
The console features a good amount of connections [[20]](https://www.copetti.org/writings/consoles/playstation-portable#bib:io-edepot):
  * **802.11b WiFi** : either connects to a hub or operates in ‘ad hoc’ mode to talk to nearby PSPs. This is similar to what the [Nintendo DS](https://www.copetti.org/writings/consoles/nintendo-ds/#freedom-of-interaction) offered.
  * **USB 2.0** : for accessories or to plug the console into a computer. In the case of the latter, the PSP is recognised as a mass storage device, providing access to the memory stick.
  * **IrDA** : stands for ‘Infrared Data Association’, similar to what a TV remote uses to change the channel. Before the release of the PSP, the infrared protocol was popular for transferring multimedia between a camera/phone and the computer. As for the PSP, however, the IrDA port went bluntly ignored.
    * As tends to happen, Sony removed it with the second revision of the PSP (2000).


### Commercial accessories
The use of a standard port, USB, enabled other companies to design accessories for this console.
[![Image](https://www.copetti.org/images/consoles/psp/io/top.fffc4aec2d9de21c44f0d8a48ad9fe4d0294a97f364faa56d72632ff85f21e46.jpg)](https://www.copetti.org/images/consoles/psp/io/top.fffc4aec2d9de21c44f0d8a48ad9fe4d0294a97f364faa56d72632ff85f21e46.jpg)Top side of the PSP (model 3000).  
Notice the two holes surrounding the mini USB port to hold an accessory.
Examples of commercialised accessories include:
  * A **microphone** for audio chatting.
  * A **GPS antenna** : apart from navigation, I don’t know what else can you do with it.
  * A **camera** : a good addition for the microphone to achieve videoconferencing. This makes sense as Skype was even embedded in the system.


The funny thing is that these gadgets were also available for Pocket PCs and PDAs as well. It makes you wonder if Sony envisioned the PSP as a _Pocket PC for youngsters_.
### Home console connectivity
After the release of the PlayStation 3, a new feature appeared on the PSP: **Remote Play**. Using a WiFi connection, the PS3 could be remotely controlled from the PSP.
This was many years before the Wii U launched, eh? Unfortunately, only a handful of PS3 games supported Remote Play, meaning users could only navigate through the menus, do some multimedia and play PlayStation 1 games.
* * *
## Operating System
Over the years, the program in charge of controlling a given console before a game starts has become more and more convoluted – mainly due to the increasing need for security and services (updatable APIs, online multiplayer, multimedia, etc.). The PSP will try to fit all of that in very constrained hardware. Now, I don’t mean to say that the result will be _mediocre_ , but many decisions are the result of balancing costs, performance and robustness.
### Architecture and design
First and foremost, the PSP contains a hidden, undocumented **4 KB ROM** inside Tachyon where the boot-loader is. In other words, upon powering on, the CPU will start by looking for instructions in there. That ROM has many names, including ‘Bootrom’, ‘Pre-IPL’ and ‘Lib-PSP iplloader’. The latter is the internal codename used by Sony.
The rest of the system is installed on **32 MB of NAND Flash memory** found in the motherboard. Here is where the majority of the PSP’s Operating System (OS) resides.
The OS is composed of the following components:
  * [Modules](https://www.copetti.org/writings/consoles/playstation-portable#tab-2-1-modules)
  * [Kernel/IPL](https://www.copetti.org/writings/consoles/playstation-portable#tab-2-2-kernelipl)
  * [Other Parts](https://www.copetti.org/writings/consoles/playstation-portable#tab-2-3-other-parts)


#### Modules
A **module** is what we would call a ‘program’ or ‘driver’ in the PC/Windows world. Once loaded, modules may reside in memory and perform the following tasks [[21]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-naked): - Expose functions to simplify access to certain hardware. - Run as a foreground program (i.e. games).
A module binary may be encrypted or decrypted. It also embeds metadata to define whether it’s a ‘user module’ or ‘kernel module’; the latter allows the new module to control privileged areas in memory (where the kernel resides).
Modules are summoned by the ‘kernel’ or ‘Visual Shell’ (VSH). User modules can execute other modules at the discretion of the kernel. This enforces security – the kernel will never load kernel modules from Universal Media Disks (UMDs), for instance.
« Previous [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-2-2-kernelipl)
#### Kernel/IPL
While this OS doesn’t contain a kernel _per se_ , it has multiple components that fill in the duties of a traditional kernel.
The first component is the **IPL** , which is loaded by the Pre-IPL and takes care of initialising the hardware. Part of the IPL, called **IDStorage** , also stores unique information about the console (such as its MAC address, serial number and UMD authentication keys) [[22]](https://www.copetti.org/writings/consoles/playstation-portable#bib:operating_system-jas). Overwriting this last area causes catastrophic results! So the UMD keys are duplicated a couple of times, to survive corruption.
The IPL then loads a set of **kernel modules** which handle low-level operations (memory management, multi-threading and file-system). They also implement memory access exceptions triggered by the MPU (remember the [segmentation paragraph](https://www.copetti.org/writings/consoles/playstation-portable#focused-memory-management)?). For the sake of simplicity, whenever I use the word ‘kernel’ in this article, I’ll be referring to these kernel modules.
Having said that, the kernel doesn’t do multitasking, but it does implement cooperative multi-threading for single processes.
The kernel will persist in memory as long as the console has power, which is related to the fact that **programs (user modules) aren’t written for bare-metal**. Instead, user modules rely on functions exposed by kernel modules. Consequently, the kernel reserves **4 MB of main RAM** and another **4 MB for ‘volatile memory’** (temporary buffer for many operations, with access granted at request). That only leaves **24 MB of main RAM** (out of 32 MB) for user programs.
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-2-1-modules) [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-2-3-other-parts)
#### Other Parts
NAND also houses other sections of the firmware.
Firstly, there’s the **Visual Shell** or ‘VSH’, which is the first thing the user notices after powering on the PSP. The VSH is a graphical user interface that allows the user to run games and other modules (only user-type ones). It is composed of multiple modules, some of which are only loaded upon request.
As a curious fact: the system call used to boot retail games will first reboot the console, and then load the executable. Possibly to unload the VSH and free up resources for the game.
Secondly, there is a second partition in NAND that stores user-related data, such as network settings. This partition is called ‘flash1’ (as opposed to ‘flash0’) and its content is referred to as **system settings**.
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-2-2-kernelipl) Next »
### Boot process
Now that we’ve identified the main parts, let’s see how they organise to put the console into a ‘working state’ once we switch it on. Security is only briefly discussed here; the next section goes into more depth.
The _complex_ boot process works as follows [[23]](https://www.copetti.org/writings/consoles/playstation-portable#bib:operating_system-ipl) [[24]](https://www.copetti.org/writings/consoles/playstation-portable#bib:cpu-naked):
  1. The main CPU’s reset vector is at `0x1FC00000`, which points to the Pre-IPL ROM inside Tachyon.
    1. The first half of the Pre-IPL tells the CPU to copy the other half to scratchpad memory and continue execution from there.
       * The Pre-IPL will now look for the next stage from either **NAND or an external memory stick**. When the latter is selected (never under normal use), the PSP enters a mode called **factory service mode**. For simplicity, we’ll focus on the normal mode (selecting NAND).
    2. The Pre-IPL initialises the NAND controller and continues execution from NAND. The second part of the Pre-IPL runs the IPL, which is encrypted, so it will be decrypted (using ‘KIRK’, more details later) and copied to eDRAM (in the Graphics Engine) as a working area.
    3. Once finished decrypting, it continues execution at eDRAM, where the decrypted IPL is.
  2. The IPL’s execution process is divided into three stages.
    1. The first stage, called the **loader** , resets the main CPU and hides the Pre-IPL ROM from the memory map. The loader also initialises minimal hardware and decompresses ‘Main.bin’, the next stage, on eDRAM.
    2. **Main.bin** focuses on initialising the rest of the hardware, including main memory. Once it finishes, it decrypts the third stage onto main memory and continues execution from there.
    3. The final stage, referred to as **payload** , loads the kernel. The kernel is stored in the form of different binaries, modules and meta-data that, once loaded into main RAM, will give life to the system. Afterwards, the interactive shell is shown.


### Visual Shell
This console debuts (at least, internationally speaking) the famous **XrossMediaBar** or ‘XMB’. This is the feature-rich GUI that was shipped with the PSP.
  * [Home](https://www.copetti.org/writings/consoles/playstation-portable#nestedtab-2-1-home)
  * [Multimedia](https://www.copetti.org/writings/consoles/playstation-portable#nestedtab-2-2-multimedia)
  * [Game](https://www.copetti.org/writings/consoles/playstation-portable#nestedtab-2-3-game)
  * [Settings](https://www.copetti.org/writings/consoles/playstation-portable#nestedtab-2-4-settings)
  * [Keyboard](https://www.copetti.org/writings/consoles/playstation-portable#nestedtab-2-5-keyboard)

[![Image](https://www.copetti.org/images/consoles/psp/xmb/main.3f3c9dada3bb82af2858c655906de0d1c2e5f4e3b21e4016c3b8455c23a084ae.jpg)](https://www.copetti.org/images/consoles/psp/xmb/main.3f3c9dada3bb82af2858c655906de0d1c2e5f4e3b21e4016c3b8455c23a084ae.jpg)Main screen (no game inserted or installed).[![Image](https://www.copetti.org/images/consoles/psp/xmb/photo.71b673d7abf01806b7a40a48969b90ae00b23c394e1b26a0018ffa33a061162d.jpg)](https://www.copetti.org/images/consoles/psp/xmb/photo.71b673d7abf01806b7a40a48969b90ae00b23c394e1b26a0018ffa33a061162d.jpg)XMB includes a photo and video viewer.[![Image](https://www.copetti.org/images/consoles/psp/xmb/game.9f6910595bdf09f76b9cfb6e176f78b584182f2d2431be5ee2f592db87413c1c.jpg)](https://www.copetti.org/images/consoles/psp/xmb/game.9f6910595bdf09f76b9cfb6e176f78b584182f2d2431be5ee2f592db87413c1c.jpg)‘Game’ category allows to run a game, manage saves or search for other PSPs (Game Sharing).  
When the user steps on the actual game item, the XMB styles itself with assets provided by the game, until the user selects another element from the category.[![Image](https://www.copetti.org/images/consoles/psp/xmb/setting.56561abe4da2fee4c4358308259adadf2504c549e302a6e8cada9a8d6dee4c8f.jpg)](https://www.copetti.org/images/consoles/psp/xmb/setting.56561abe4da2fee4c4358308259adadf2504c549e302a6e8cada9a8d6dee4c8f.jpg)‘Settings’ category provides lots of customisation options.  
Some items group many settings controls.[![Image](https://www.copetti.org/images/consoles/psp/xmb/keyboard.e06bc606c91eb0fb380270cb7176a7aa2f67116ca0c92216d4cc37ccd26d5dc0.jpg)](https://www.copetti.org/images/consoles/psp/xmb/keyboard.e06bc606c91eb0fb380270cb7176a7aa2f67116ca0c92216d4cc37ccd26d5dc0.jpg)This is how you type in this console, old-school cellphone style.
From a human-computer interaction standpoint, the XMB’s design reveals very interesting approaches for solving many interaction challenges (such as navigating around many depths of information, avoiding flooding the user with options and fitting all these solutions in a 4.3” screen). In essence, information is organised by ‘categories’ and ‘elements’; and the D-pad is the key to navigate through them. The left and right arrows switch between categories, and the up and down arrows select an element from within a category. It’s worth pointing out that all categories are found within the same hierarchy level. So, no entry is shown superimposed over the rest (impeding the insertion of attention-stealing advertisement and whatnot).
On another topic, the XMB provides customisation options, such as changing the background colour and re-arranging items. Moreover, it provides access to multimedia services and, of course, allows the user to load up the game (whether from a UMD or memory stick).
There’s also a file viewer embedded, which is used for both multimedia and save management.
### Updatability
As we’ve seen before, everything except the Pre-IPL is stored in writable storage, and thus is ‘updatable’. Sony distributed firmware updates in the form of downloadable files. Users could either manually download them or use the ‘system update’ assistant from the XrossMediaBar to automatically download (using WiFi) and install them.
[![Image](https://www.copetti.org/images/consoles/psp/xmb/update.b1f36c91dd0572e2399f7676c583a77a67a156a0aa155c42161c6a648b213f7c.jpg)](https://www.copetti.org/images/consoles/psp/xmb/update.b1f36c91dd0572e2399f7676c583a77a67a156a0aa155c42161c6a648b213f7c.jpg)System Update ‘Wizard’.
Some updates strengthened the PSP’s security system by adding more layers of encryption to the boot process and integrity checks on kernel modules.
From the developer’s standpoint, some updates enhanced the APIs by adding more functions and correcting existing ones. Games were therefore strongly tied to the system version they were developed for, and users would have to update to play newer games. However, new updates were always backwards compatible, so an old game should never break on an updated system (in theory).
From the user’s perspective, some updates brought new services, like a web browser, RSS reader and so forth. After the release of the PlayStation 3, many online applications were ported to the PSP, such as the ‘PlayStation Store’ and ‘Remote Play’.
* * *
## Games
For the first time in this series, games developed for this console are not written for bare-metal: instead of relying on memory address and ports, they would have to call modules to perform operations on the hardware. The APIs found in the official SDK are modelled after this design.
### Development ecosystem
The development toolkit provided by Sony to game studios was developed by SN Systems (the same author of the PS1 and PS2 kits). The software kit required a setup with either Windows XP and Cygwin or CentOS Linux.
In this kit we could find:
  * An **SDK** : contained C++ libraries that linked to a particular version of the firmware (as they depend on the modules installed).
  * A choice of **two compilers** : a variant of the GCC compiler called ‘psp-gcc’, or one developed by SN Systems called ‘SVCPSP’ (‘SVC’ targeting the PSP).
  * The **GDB debugger**.
  * SN System’s **assembler** , **linker** and **archiver**. The latter generates PSP executables.
  * A **plugin for Visual Studio 2005 and 2008** , so developers could use Microsoft’s IDE for PSP development.


Initially, Sony only provided an emulator to test PSP software. This was later replaced with the **PSP Hardware Tool** : a PC-like tower connected to a dummy PSP case (similar to the [Nintendo DS kit](https://www.copetti.org/writings/consoles/nintendo-ds/#tab-5-1-the-hardware)). The devkit connected to the workstation using a piece of software called **ProDG** (only available on Windows).
### Storage medium
The PS1 and PS2 featured two types of storage: a read-only disc for loading games, and a re-writable ‘Memory Card’ for storing saves and executables. The PSP continued this tradition using different methods. Considering it was their first -mainstream- portable console, how did Sony manage to find the right medium for each job? Well, taking into account they were the creators of the _BetaMax_ , _MiniDisc_ and so forth, you can guess what they did this time… introduce _even more_ formats.
  * [UMD Discs](https://www.copetti.org/writings/consoles/playstation-portable#tab-3-1-umd-discs)
  * [Memory Stick Duo](https://www.copetti.org/writings/consoles/playstation-portable#tab-3-2-memory-stick-duo)


#### UMD Discs
[![Image](https://www.copetti.org/images/consoles/psp/retail.000ecee3e13ff9f121df011b11d37b2e5547229ef51b16b1c9848a21bead2920.jpg)](https://www.copetti.org/images/consoles/psp/retail.000ecee3e13ff9f121df011b11d37b2e5547229ef51b16b1c9848a21bead2920.jpg)Typical retail game.
CDs and DVDs are too big, and easily copiable. On the other hand, conventional readers won’t work in a shaky environment (those who tried listening to an audio CD on a Walkman while _walking_ know what I’m talking about). So, Sony’s solution was a new invention from the ground up called **Universal Media Disc** , a proprietary medium.
UMDs hold either **900 MB or 1.8 GB** depending on whether they are single-layered or dual-layered, respectively. UMDs not only differ physically from a DVD or MiniDVD, but they also contain a different internal structure. Apart from games, Sony published the ‘UMD video’ and ‘UMD audio’ specifications, allowing other distributors to ship their content to PSP users – remember, this is the year 2004 (when the _iPod Photo_ had a 2” display).
These discs are presented with an **non-removable caddy** ; the centre is magnetic so it attaches itself to the reader’s motor once the disc is inserted.
« Previous [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-3-2-memory-stick-duo)
#### Memory Stick Duo
[![Image](https://www.copetti.org/images/consoles/psp/io/memory_stick.81e9274f19c56fdfd4f866b3dfa14c2ed8c8967a8ec0afa7c21cac565ac75630.jpg)](https://www.copetti.org/images/consoles/psp/io/memory_stick.81e9274f19c56fdfd4f866b3dfa14c2ed8c8967a8ec0afa7c21cac565ac75630.jpg)A Memory Stick next to a conventional SD card.
The ‘portable’ equivalent of the Memory Card is the **Memory Stick Pro Duo** , another product of Sony’s insistence to bring another medium to a flooded market (remember the massive number of options back then? Even [flashcarts](https://www.copetti.org/writings/consoles/game-boy-advance/#flashcarts) accommodated many of them). This was released during the boom in consumer photography and cellphones, when people wanted lots of storage for a cheap price; and just before the SD card took over.
The Memory Stick, like the rest, is a protocol that interfaces internal memory (like Flash) with any peripheral in a way that’s convenient. So, you may swap cards between the computer and the camera without having disassemble anything. The ‘Pro Duo’ variant (used by the PSP) has a capacity of **up to 32 GB** and **1.23 MB/s read** and **0.54 MB/s write speed**.
The PSP relies on the Memory Stick to store user-related content, such as saves, media and games. It’s formatted with the FAT32 file system. The controller embedded in the Memory Stick can include MagicGate DRM.
The contents are not memory mapped: the file system is accessed through system calls (kernel modules).
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-3-1-umd-discs) Next »
### Network services
Eventually, Sony caught up with the competition and improved its online infrastructure. They even offered services not yet provided by Microsoft or Nintendo.
  * [PlayStation Network](https://www.copetti.org/writings/consoles/playstation-portable#tab-4-1-playstation-network)
  * [PlayStation Store](https://www.copetti.org/writings/consoles/playstation-portable#tab-4-2-playstation-store)
  * [Updatable content](https://www.copetti.org/writings/consoles/playstation-portable#tab-4-3-updatable-content)


#### PlayStation Network
[![Image](https://www.copetti.org/images/consoles/psp/xmb/network.ea7492c1c4f5335644b55d7e7e5b5b665a730db8e18d9e454e136b8d59ffe68d.jpg)](https://www.copetti.org/images/consoles/psp/xmb/network.ea7492c1c4f5335644b55d7e7e5b5b665a730db8e18d9e454e136b8d59ffe68d.jpg)PSN category in XMB.
In answer to Microsoft’s [Xbox Live](https://www.copetti.org/writings/consoles/xbox/#network-service) and Nintendo’s [Nintendo WiFi Connection](https://www.copetti.org/writings/consoles/nintendo-ds/#network-service), Sony had its own online infrastructure… **PlayStation Network** , or PSN.
This service superseded the primitive [DNAS](https://www.copetti.org/writings/consoles/playstation-2/#network-service), previously deployed for the PlayStation 2. One of the additions was the use of a centralised authentication system.
Users could register a free PSN account using the console; this enabled them to play with other people around the globe using WiFi connection.
It’s worth mentioning that at first, the PSP didn’t include many online services. This changed drastically with the release of the PlayStation 3, but I guess this is a story for a later article…
« Previous [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-4-2-playstation-store)
#### PlayStation Store
[![Image](https://www.copetti.org/images/consoles/psp/xmb/store.e85d52bda532a6e09340906be9acd6bd9f56dd8c5a32954c177a6d707c644f98.jpg)](https://www.copetti.org/images/consoles/psp/xmb/store.e85d52bda532a6e09340906be9acd6bd9f56dd8c5a32954c177a6d707c644f98.jpg)PlayStation Store.
Another thing that followed after the debut PlayStation Network was the **PlayStation Store**. As the name indicates, it’s an online store that allows users to acquire games digitally and download them onto their Memory Stick.
I suppose this was a great relief for small game studios, as physical distribution always implied a significant cost, which would eventually [impact](https://www.copetti.org/writings/consoles/nintendo-64/#games) the price of the game. Strangely enough, a later model of the PSP called ‘PSP Go’ enforced this move away from physical media – by removing the UMD reader, it could only play games acquired from the PlayStation Store.
Later on, the game catalogue drastically expanded with the arrival of **[PS1 games](https://www.copetti.org/writings/consoles/playstation/#games)**. These were downloaded to the Memory Card and played like any other digital game. PS1 binaries on the PSP worked with the use of **software emulation** ; Sony embedded an in-house emulator in the system to make all this work seamlessly.
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-4-1-playstation-network) [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-4-3-updatable-content)
#### Updatable content
[![Image](https://www.copetti.org/images/consoles/psp/xmb/game_update.83dd1dbb7fa577a110653940e7a6d94a8012096db7d764ea171a39c3c486c85e.jpg)](https://www.copetti.org/images/consoles/psp/xmb/game_update.83dd1dbb7fa577a110653940e7a6d94a8012096db7d764ea171a39c3c486c85e.jpg)‘Update game’ option in XMB.
Last but not least, online services provided the opportunity to **download game patches** (in the form of ‘updates’) directly to the console.
However, not many games used this feature. This is hard to conceive nowadays, as large game updates tend to be published before the game hits the store…
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-4-2-playstation-store) Next »
* * *
## Anti-Piracy and Homebrew
Just because this is a portable console doesn’t mean it should have weaker security than the PS2. It’s quite the opposite in all senses – the security system implemented on the PSP is very diverse, with some parts still remaining a mystery to this day.
Now, we all know by now that its implementation contained pitfalls that eventually lead to Homebrew and piracy, but considering it was released in 2004 and it’s a portable console, you may find that some algorithms bundled are state-of-the-art compared to the competition.
### Physical security
I’m going to describe the three main chips that compute security-related operations. The algorithms can be pretty complicated for first-timers, but I’ll try to give a quick overview. Don’t forget to check out the bibliography if you find it interesting, as this writing is primarily focused on the PSP itself.
Throughout the explanations, keep in mind that none of this information was documented by Sony for security reasons, in addition to labelling security-related routines with silly names.
Furthermore, I won’t be able to go over each cypher system, as it’s a tortuous topic and would divert the article from its main goal. Nonetheless, I invite you to learn about the logic behind each algorithm from other sources.
  * [KIRK](https://www.copetti.org/writings/consoles/playstation-portable#tab-5-1-kirk)
  * [Lepton](https://www.copetti.org/writings/consoles/playstation-portable#tab-5-2-lepton)
  * [SPOCK](https://www.copetti.org/writings/consoles/playstation-portable#tab-5-3-spock)


#### KIRK
To start with, we got **KIRK** , another component inside Tachyon. KIRK is the implementation in hardware of the following algorithms (think of it as an accelerator) [[25]](https://www.copetti.org/writings/consoles/playstation-portable#bib:anti_piracy-kirk) [[26]](https://www.copetti.org/writings/consoles/playstation-portable#bib:anti_piracy-keys):
  * **Advanced Encryption Standard (AES) encryption and decryption** : a symmetric encryption system that operates with a given key. KIRK also provides a key vault of 128 keys and a master key, both 128 bits long, to encrypt/decrypt data.
  * **ECDSA** : an asymmetric encryption system. It includes two functions:
    * Public-private key generation: used for encrypting and decrypting user data, such as save files.
    * Signature verification: checks and decrypts data encrypted by Sony (it stores a public key).
  * **SHA-1** : generates a hash value from data. ECDSA depends on SHA during signature verification (confirms that the original data hasn’t been tampered with).
  * **Cipher-based Message Authentication Code (CMAC)** : another algorithm used to decrypt and verify the integrity of the encrypted data (whether it comes from Sony or not) using a shared key. It relies on AES for decryption.
  * **Pseudo-random number generation** : As the name indicates, it (attempts) to generate an unpredictable number.


In short, the CPU sends commands to KIRK (i.e. ‘encrypt this string with algorithm x and key y’). KIRK can behave like a bus master as well, so it stores the results on main RAM right away.
« Previous [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-5-2-lepton)
#### Lepton
As you know, UMD discs are not easily duplicated, but their contents are also stored in an encrypted form. Users will never notice this, however, since the decryption process is performed by hardware too.
Living alongside Tachyon, another System-on-Chip known as **Lepton** controls the UMD drive, and serves as a middle-man between the main CPU and UMD content.
Lepton contains an enormous amount of circuitry – you may even consider it another computer living inside the PSP. This component includes its own CPU, a DSP for decoding, 480 KB of memory (as buffer) and finally, 384 KB of ROM for storing its firmware.
The main CPU communicates to Lepton using the ATAPI protocol, an interface traditionally used for plugging conventional CD/DVD drives to PCs. The main difference, however, is that the Lepton will only decrypt data from a UMD if the disc is identified as authentic.
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-5-1-kirk) [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-5-3-spock)
#### SPOCK
Apart from the encryption system handled by Lepton, a UMD’s sectors are encrypted using AES. **SPOCK** is another block found next to KIRK that focuses on decrypting each sector of the UMD disc.
Inside NAND Flash, IDStorage stores an encrypted key known as the ‘master key’. SPOCK contains a hardwired key used to decrypt it. The decrypted master key is then used by SPOCK to decrypt another key found in the UMD. The latter key is then used to read each sector. _Easy-peasy!_
By the way, even though SPOCK is found within Tachyon, it’s operated by Lepton.
To sum up, having these routines in hardware allows the system to execute games without consuming general-purpose resources to apply encryption/decryption.
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-5-2-lepton) Next »
### Software security
The operating system will use the hardware provided to compose a security system. Overall, the software is protected using the following principles:
  * **Chain of trust** : The Pre-IPL, the first stage of the boot process, is a read-only piece of code written by Sony and embedded during manufacturing. Anything that the Pre-IPL approves is deemed trustworthy, and so are the subsequent programs executed.
  * **Signed executables** : not only are executables encrypted, but they are also signed with keys that only Sony knows, ensuring that tampered data can’t be re-signed.
  * **Obscure hardware** : KIRK, SPOCK and Lepton are undocumented and obfuscated blocks of silicon that won’t expose which algorithms are applied and how.
  * **Developer-proof security** : the MMU’s privilege modes will restrict access to sensible memory locations, even with the existence of user-level exploits on retail games (which lead to arbitrary code execution).


### Defeat
Despite all the security, it seems that hackers never gave up on this console (maybe because the number of benefits made it very attractive for Homebrew development?). Please note that the amount of development in this area is outstanding, so I had to draw a line somewhere. Thus, only huge discoveries are mentioned here. In any case, playstationdev.wiki keeps a good archive of every single one.
  * [Early blunders](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-1-early-blunders)
  * [Downgrading](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-2-downgrading)
  * [Pandora](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-3-pandora)
  * [CFW and beyond](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-4-cfw-and-beyond)


#### Early blunders
After the release of the PSP in Japan, it was a matter of time before userland exploits emerged. Some of them used the flawed security found in early versions of the firmware:
  * ‘Wipe Out’ embedded a web browser to access downloadable content. It wasn’t protected against **DNS attacks (domain hijacking)** , allowing users to browse any URL in the world-wide-web.
    * Later on, it was discovered that the browser’s URL entry didn’t verify the input. So, entering `file:///disc0:/` as URL would **list the contents of the UMD** , already unencrypted. This enabled hackers to inspect PSP executables and reverse engineer them.
  * The first revision of the system **didn’t check for signatures** in the executables stored in the memory stick, allowing to run custom user modules (not kernel ones).
    * This was probably accidental as it’s common practice to use a debug version of the system (without signature checks) for development purposes. So they may have rushed into release and forgotten to re-activate the checks, like [Microsoft](https://www.copetti.org/writings/consoles/xbox/#tab-5-2-bootstrap-search) did.
  * After this was patched, hackers discovered **a flaw in the file system implementation** and used it to keep running unsigned code. In a nutshell, the user would have to duplicate the folder containing the executable, add an extra `%` at the end of the name of the second folder and strategically reorganise the contents of both folders.


These early blunders helped to build a knowledge base of the inner workings of the PSP, which led to more attack vectors and software routines built to interact with the hardware (keep in mind only game studios had access to official SDKs and documentation).
As with any other cat and mouse game, Sony responded with more system updates (which were required by new games) while newer exploits (the so-called ‘TIFF’, ‘GTA’ exploit and so forth [[27]](https://www.copetti.org/writings/consoles/playstation-portable#bib:anti_piracy-homebrew)) kept appearing. It’s worth mentioning that these were only considered ‘Homebrew launchers’ as kernel access wasn’t obtained yet.
« Previous [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-2-downgrading)
#### Downgrading
[![Image](https://www.copetti.org/images/consoles/psp/downgrader.18f42043d258300ea81d9e241ef8e9e5cca6f3d008e48cfb85c3b922832541a4.jpg)](https://www.copetti.org/images/consoles/psp/downgrader.18f42043d258300ea81d9e241ef8e9e5cca6f3d008e48cfb85c3b922832541a4.jpg)Chronoswitch downgrader, a modern downgrade tool.
As soon as Sony gained momentum with strong firmware updates with security patches and attractive features (i.e. a web browser), old versions became some sort of promised land, where advanced users enjoyed the ability to run their Homebrew. However, acquiring a PSP with that system version became increasingly challenging. Thus, ‘downgrading’ quickly gained popularity. Downgrading is the opposite of upgrading, consisting of replacing the current firmware installed with an earlier (and better exploited) version.
A common approach for performing a downgrade consists of executing an exploit that would trick the system into installing an old update file. This wasn’t easy, as it depended on an ever-shrinking pool of exploits for the most recent version.
Eventually, two ‘modchips’ reached the market: ‘Undiluted Platinum’ and ‘PSP-Devolution’. Both shipped with a separate NAND chip used as secondary NAND storage, enabling the user to boot a secondary (and exploitable) firmware, or replace the primary one. This approach is only supported on the PSP model 1000, as later ones unified Tachyon and the NAND + DDR SDRAM package.
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-1-early-blunders) [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-3-pandora)
#### Pandora
The cat and mouse game was the order of the day until the so-called ‘Pandora’ arrived.
The ‘Pandora battery method’ is a popular (and respected) collection of achievements. It managed to bypass most of the security layers, and focused on where Sony could not react quickly: the Pre-IPL. This is what Pandora managed to succeed in [[28]](https://www.copetti.org/writings/consoles/playstation-portable#bib:anti_piracy-pandora):
  * **Find a way of entering entering ‘Service Mode’** : by tampering with the PSP’s removable battery, which had some circuitry attached for identification purposes, hackers discovered that overriding its serial number value to `0xFFFFFFFF` triggered service mode at boot time. Thus, the Pre-IPL would look for a secondary system in the Memory Stick. The modified battery was referred to as **JigKick** or ‘Pandora’ Battery.
    * Users could create a Jigkick battery with a hacked PSP, or by desoldering the ground pin of the battery’s EEPROM. The latter is riskier, taking into account casual users are disassembling a Lithium battery! Thus, some companies distributed their own ‘Pandora battery’ maker.
    * A Jigkick battery works like any other battery. However, when inserted, the PSP will always boot from the Memory Stick.
  * **Trick ‘Service mode’ into loading fake/unsigned firmware** : the next step was to find a way to load a fake IPL in service mode (it still has to be encrypted and signed to work). Well, hackers found a way, by embedding an unencrypted payload next to the encrypted block. The Pre-IPL would try to validate it (due to the Pre-IPL not checking that the encrypted block is 1 KB long). The encrypted section had to be crafted in a way that, once decrypted, will tell the Pre-IPL to ‘jump 100 bytes down’. This bypassed the security routines and redirected execution to the payload, enabling anyone to **execute code with maximum privileges** in service mode. This reminds me of what happened to the [Wii](https://www.copetti.org/writings/consoles/wii/#the-fall-of-encryption).
    * The custom IPL needed to be executed from a specific sector in the Memory Stick. A Memory Stick with a custom IPL installed to this location is called **Magic Memory Stick**. Special programs were developed, allowing any user to create one.


What remained was to embed a useful payload. Popular options included a ‘de-bricker’ which (re)installed a clean official firmware onto the PSP (thereby repairing it if the NAND was previously corrupted), a ‘downgrader’, or a custom firmware installer (more details later).
Don’t forget that all this was a tremendous task, especially if we take into account that KIRK wasn’t reverse engineered and the encrypted block that makes the Pre-IPL ‘jump’ had to be brute-forced.
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-2-downgrading) [Next »](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-4-cfw-and-beyond)
#### CFW and beyond
[![Image](https://www.copetti.org/images/consoles/psp/xmb/cfw.e2577cc421c2454a054827201847de465af53649a052ff9dbce9e7063aa78482.jpg)](https://www.copetti.org/images/consoles/psp/xmb/cfw.e2577cc421c2454a054827201847de465af53649a052ff9dbce9e7063aa78482.jpg)Some CFWs include special modules to operate low-level options.
The Pandora method represented a big blow for Sony – it was an effective bootrom exploit, and just like the [Nintendo DS](https://www.copetti.org/writings/consoles/nintendo-ds/#tab-7-3-native-slot-1), fixes would only arrive in the form of new hardware revisions.
Furthermore, before Pandora was published, so-called **Custom Firmware** or ‘CFW’ arrived. CFW is an official firmware with modifications applied (such as Homebrew modules). These customisations enjoyed kernel privileges and, as you may guess, they had complete control of the console. Examples of new modules included ISO loaders, signature disablers, low-level CPU management, a ‘plugin’ loader (to add more customisations without re-installing the firmware), and many, many more. Lots of hackers crafted their own flavour, such as M33, PRO and ME.
A CFW can be installed on top of the current firmware with the help of any kernel-level exploit (this was the earliest method). However, it can only be automatically booted with exploits previously used by Pandora to bypass signature checks. Otherwise, users need to rely on cat-and-mouse exploits to reboot to a CFW. That’s why the latest PSP models weren’t able to kickstart a CFW using the _good-old_ methods.
In the end, the last straw was when the [security system](https://www.copetti.org/writings/consoles/playstation-3/#os-security-hierarchy) of the [PlayStation 3](https://www.copetti.org/writings/consoles/playstation-3/) was [hacked](https://www.copetti.org/writings/consoles/playstation-3/#tab-9-4-the-fall-of-encryption), as it contained the **private keys used to decrypt PSP executables** (the PS3’s OS includes a PSP emulator). This allowed anyone to sign userland software and embed a kernel exploit to produce CFW installers and/or CFW loaders, for instance.
In recent developments, it was discovered that the latest firmware contains a kernel exploit during the boot process, which could be used to kickstart a CFW of choice. This was packaged in an solution called **Infinity 2** [[29]](https://www.copetti.org/writings/consoles/playstation-portable#bib:anti_piracy-davee).
To sum it up, Sony was right when they claimed the UMDs were un-hackable. After all, hacking was achieved instead thanks to (many) flaws in software.
[« Previous](https://www.copetti.org/writings/consoles/playstation-portable#tab-6-3-pandora) Next »
### Homebrew encouragement
Not only Homebrew development centred on breaking security mechanisms, but there were also communities committed to providing Homebrew developers with the necessary tools to build their software without legal repercussions. For instance, the pspdev group published an open-source SDK called **PSPSDK** that replicated many of the official interfaces and didn’t enforce previous restrictions imposed by Sony.
PSPSDK also includes a toolkit to handle the compilation and packaging process, just like the official SDK but targeting a PSP running a CFW instead.
* * *
## That’s all folks
[![Image](https://www.copetti.org/images/consoles/psp/mypsp.38961ffb3900f95c8c02bac465e7794bd5c773cfe61a2e9acfc20fb21fb54f79.jpg)](https://www.copetti.org/images/consoles/psp/mypsp.38961ffb3900f95c8c02bac465e7794bd5c773cfe61a2e9acfc20fb21fb54f79.jpg)The PSP acquired for this article.  
This is what grownups used to buy if they wanted to look cool 😉 (I had a DS).
There you go, you’ve just finished reading about the last portable console before smartphones and tablets took over! I think this gives us an idea of what services/features users were expecting from portable handhelds in the early noughties – and how this evolved during the next decade.
Nevertheless, I want to thank the PSP Homebrew Community discord for not only taking the time to proofread this _endless_ article, but also to enlighten me with even more information. Various members of that group have dedicated great effort to develop free tools and Homebrew applications to expand the capabilities of this console. My acknowledgement is also directed to all the authors who produced the documents listed in the sources. It took me ~3 months to write this article, but it was possible thanks to the combined years of work that other people dedicated to reverse-engineer this console.
As for the next article, I’ll need to first take one month or two to focus on all the issues and requests submitted on the [GitHub repo](https://github.com/flipacholas/Architecture-of-consoles) and do some maintenance work on the site, but rest assured I’m striving to make the next writing as complete as this one!
Until next time!  
Rodrigo
* * *
## Contributing
This article is part of the [Architecture of Consoles](https://www.copetti.org/writings/consoles/) series. If you found it interesting then please consider donating. Your contribution will be used to fund the purchase of tools and resources that will help me to improve the quality of existing articles and upcoming ones.
[![Donate with PayPal](https://www.copetti.org/images/paypal_donate.png)](https://www.paypal.com/donate/?hosted_button_id=3GXQA6XPL7G3S)
[![Become a Patreon](https://www.copetti.org/images/patreon.png)](https://www.patreon.com/copetti)
You can also buy the [book editions](https://www.copetti.org/writings/consoles/materials/book/) in English. I treat profits as donations.
[![eBook edition](https://www.copetti.org/images/consoles/books/ebooks_banner.0d180c0136e4c9345bc0ab4f7a0224849a292326d2679d610ea945054383a996.jpg)](https://www.copetti.org/writings/consoles/materials/book/)
Big thanks to the following people for their donation:
```
- Alexander Perepechko
- Andreas Kotes
- Ben Morris
- Cirilla Rose
- Colin Szechy
- Daniel Cassidy
- David Portillo
- Elizabeth Parks
- Eric Haskins
- eurasianwolf
- Grady Haynes
- Guillermo Angeris
- Josh Enders
- Luke Wren
- Matthew Butch
- Olivier Cahagne
- petey893
- Racri
- Stuart Hicks
- Thomas Finch
- Thomas Peter Berntsen
- Tim Cox
```

Alternatively, you can help out by [suggesting changes](https://github.com/flipacholas/Architecture-of-consoles) and/or [adding translations](https://github.com/flipacholas/Architecture-of-consoles).
* * *
## Copyright and permissions
This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). You may use it for your work at no cost, even for commercial purposes. But you have to respect the license and reference the article properly. Please take a look at the following guidelines and permissions:
Article information and referencing
For any referencing style, you can use the following information:
  * **Title of article** : PlayStation Portable (PSP) Architecture - A Practical Analysis
  * **Author** : Rodrigo Copetti
  * **URL** : <https://www.copetti.org/writings/consoles/playstation-portable/>
  * **Date of publication** : April 21, 2021
  * **Last modified** : August 25, 2025


For instance, to use with BibTeX:
```
@misc{copetti-psp,
    url = {https://www.copetti.org/writings/consoles/playstation-portable/},
    title = {PlayStation Portable (PSP) Architecture - A Practical Analysis},
    author = {Rodrigo Copetti},
    year = {2021}
}

```

or a IEEE style citation:
```
[1]R. Copetti, "PlayStation Portable (PSP) Architecture - A Practical Analysis", Copetti.org, 2021. [Online]. Available: https://www.copetti.org/writings/consoles/playstation-portable/. [Accessed: day- month- year].

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
  * wikibooks.org, [PSP homebrew history](https://en.wikibooks.org/wiki/PSP/Homebrew_History). [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:27)
  * pastie.org, [UMD keys decrypted](https://web.archive.org/web/20141201091221/http://pastie.org/1467912).
  * PPSSPP Project, [Kirk_engine.c](https://github.com/hrydgard/ppsspp/blob/a1964ca1a108b1340e54ae30262f317c9dd6999b/ext/libkirk/kirk_engine.c). Github. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:25)
  * PSP Developer Wiki, [Keys — PSP developer wiki](https://playstationdev.wiki/pspdevwiki/index.php?title=Keys&oldid=11336). 2021. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:26)
  * Fanjita, [Pandora’s battery](https://web.archive.org/web/20070828091049/http://www.noobz.eu/joomla/news/pandoras-battery.html/) (Official announcement). Archived. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:28)
  * Davee, [6.61 infinity - an explanation](https://www.lolhax.org/2017/09/24/6-61-infinity-an-explanation/). [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:29)


### Audio
  * PPSSPP Project, [SasAudio.cpp](https://github.com/hrydgard/ppsspp/blob/0c40e918c92b897f745abee0d09cf033a1572337/Core/HW/SasAudio.cpp). Github. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:18)
  * PPSSPP Project, [SimpleAudioDec.cpp](https://github.com/hrydgard/ppsspp/blob/0c40e918c92b897f745abee0d09cf033a1572337/Core/HW/SimpleAudioDec.cpp). Github. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:17)


### CPU
  * groepaz/hitmen, [Yet another PlayStationPortable documentation](http://hitmen.c02.at/files/yapspd/psp_doc/). [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:4)
  * Tom Foremski, [SGI to sell 6 million MIPS technology shares](https://www.electronicsweekly.com/news/archived/resources-archived/sgi-to-sell-6-million-mips-technology-shares-1999-05/). [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:1)
  * TyRaNiD, [The naked PSP](https://uofw.github.io/upspd/docs/software/naked_psp.pdf). ps2dev.org. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:24)
  * PCMag India staff, [Sony PSP specs](https://in.pcmag.com/gallery/273/sony-psp-specs). [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:11)
  * Alex Marshall, [PSPTEK](http://daifukkat.su/docs/psptek/). [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:9)
  * PPSSPP Project, [MediaEngine.cpp](https://github.com/hrydgard/ppsspp/blob/0c40e918c92b897f745abee0d09cf033a1572337/Core/HW/MediaEngine.cpp). Github. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:10)
  * Bryan Fletcher, [Programming the PlayStation portable (PSP)](https://www.gdcvault.com/play/1013616/Programming-the-PlayStation-Portable). GDCVault. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:14)
  * MIPS, MIPS architecture for programmers - volume i-a: Introduction to the MIPS64® architecture - revision 6.01. 2014. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:2)
  * MIPS, MIPS32 4K - processor core family - software user’s manual - revision 01.18. 2004. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:6)
  * pspdev, [Psptoolchain - gcc-4.9.3-PSP.patch](https://web.archive.org/web/20210423135450/https://github.com/pspdev/psptoolchain/blob/master/patches/gcc-4.9.3-PSP.patch) (Archived). Github. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:3)
  * Computer History Museum, [MIPS: Risking it all on RISC](https://www.youtube.com/watch?v=3paiCK3dlK0). Youtube. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:8)


### Graphics
  * pspdev, [Graphics utility library - PSPSDK 1.0+beta2](https://pspdev.github.io/pspsdk/group__GU.html). [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:15)


### I/O
  * edepot.com, [PSP secrets](http://www.edepot.com/reviews_sony_psp.html). [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:20)
  * NIL:’s white page, [Interfacing with the PSP remote port](https://nil.rpc1.org/psp/remote.html). [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:16)
  * SilverSpring, [Motherboard IC’s](http://uofw.github.io/upspd/docs/SilverSpring_Blog/my.malloc.us/silverspring/motherboard-ics/index.html).


### Operating System
  * jas0nuk, [IdStorage keys and their uses + regeneration [TECHNICAL DISCUSSION]](https://archive.ph/pxuGj). LAN.ST. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:22)
  * PSP Developer Wiki, [Initial program loader — PSP developer wiki](https://playstationdev.wiki/pspdevwiki/index.php?title=Initial_Program_Loader&oldid=10580). 2020. [↩︎](https://www.copetti.org/writings/consoles/playstation-portable#bibref:23)


### Other Media
  * Zophar gallery, [Raw music files](https://www.zophar.net/).
  * The Models Resource, [3D models](https://web.archive.org/web/20200216025504/https://www.models-resource.com/). Archived.


### Photography
  * Evan Amos, [The vanamo online game museum](https://commons.wikimedia.org/wiki/User:Evan-Amos).
  * Rodrigo Copetti (Me), [Diagrams, casual photos and game screenshots](https://www.copetti.org/).
  * Kisscc0, [Memory stick icon](https://www.kisscc0.com/clipart/sony-corporation-flash-memory-cards-sony-dsc-w1-me-i6mxg4/).


* * *
## Changelog
It’s always nice to keep a record of changes. For a complete report, you can check the [commit log](https://github.com/flipacholas/Architecture-of-consoles/commits/master/articles/playstation-portable.Rmd.md). Alternatively, here’s a simplified list:
```
### 2024-02-21
- Extended CPU section with more information about the MIPS line
### 2021-08-30
- General round of spelling and grammatical corrections, see https://github.com/flipacholas/Architecture-of-consoles/pull/40 (thanks @FormulatedEdits)
### 2021-04-23
- Corrected sampling rate value, thanks /r/cracyc
- Improved statement about Infinity, thanks @davee and @balika011
### 2021-04-21
- Oven-ready!
### 2021-04-19
- Release Candidate draft
- Fixed grammar and sorted out the rest
### 2021-04-17
- Second draft finished. Thanks @artart78, @TBS-Frain_Breeze, @Draan, @Hedge and @balika011 from pspdev
- TODO: Check grammar (again) and fix the remaining photography
### 2021-04-11
- First draft finished.
- Carlos, you need to get a PS4 and play Persona, no fuzz!
```

* * *
[« Nintendo DS Architecture](https://www.copetti.org/writings/consoles/nintendo-ds/) [Xbox 360 Architecture »](https://www.copetti.org/writings/consoles/xbox-360/)
![Rodrigo Copetti](https://www.copetti.org/favicon/favicon.png)
### Rodrigo Copetti
I hope you have enjoyed this article! If you want to know more about the author [tap here](https://www.copetti.org/about/) and if you would like to support him [tap here](https://www.copetti.org/support/) instead
[Tweet ](https://twitter.com/intent/tweet?text=PlayStation%20Portable%20%28PSP%29%20Architecture%20%7c%20A%20Practical%20Analysis%20https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fplaystation-portable%2f)[Share ](javascript:void\(0\))[Share ](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fplaystation-portable%2f&title=PlayStation%20Portable%20%28PSP%29%20Architecture%20%7c%20A%20Practical%20Analysis&summary=An%20in-depth%20analysis%20that%20explains%20how%20this%20console%20works%20internally&source=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fplaystation-portable%2f)[Share](https://reddit.com/submit?url=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fplaystation-portable%2f&title=PlayStation%20Portable%20%28PSP%29%20Architecture%20%7c%20A%20Practical%20Analysis)
[Switch to classic edition](https://classic.copetti.org/writings/consoles/playstation-portable/)
Rodrigo Copetti © 2025 [](https://www.copetti.org/index.xml)
[About the website and its content](https://www.copetti.org/disclaimer/)
rsslinkedintwitterblueskygithub facebookreddit
