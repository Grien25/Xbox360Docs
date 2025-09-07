# Nintendo 64 Architecture | A Practical Analysis

**Source:** https://www.copetti.org/writings/consoles/nintendo-64

[Home](https://www.copetti.org/)
[Consoles](https://www.copetti.org/writings/consoles/)
[About](https://www.copetti.org/about/)
[Support](https://www.copetti.org/support/)
# Nintendo 64 Architecture
## A practical analysis by Rodrigo Copetti
[](https://github.com/flipacholas/Architecture-of-consoles)[](https://crowdin.com/project/architecture-of-consoles)[](https://www.copetti.org/writings/consoles/materials/readings/)[](https://www.copetti.org/writings/consoles/nintendo-64)
If you use accessibility tools or old browsers, [switch to the ‘classic’ edition](https://classic.copetti.org/writings/consoles/nintendo-64/).
🇬🇧 - English 🇵🇱 - Polski 🇪🇸 - Español 🇨🇳 - 简体字 👋 - Add translation
* * *
Book edition
[![eBook edition](https://www.copetti.org/images/consoles/_covers/en/nintendo-64_hu_92a987d91159814.jpg)](https://www.copetti.org/writings/consoles/materials/book/)
This article is also published in many bookstores for the benefit of offline readers. The eBooks are DRM-free, while the printed editions compile multiple articles and feature original photography at full resolution.
You can find printed compilations [here](https://www.amazon.com/dp/B0F4P5RB25?binding=paperback), and individual eBooks at [Amazon Kindle](https://www.amazon.com/dp/B0B5VM3NHS), [Apple Books](https://books.apple.com/us/author/rodrigo-copetti/id1632545359?see-all=books), [Kobo](https://www.kobo.com/us/en/search?query=Architecture+of+Consoles%3a+A+Practical+Analysis&fcsearchfield=Series&seriesId=7e46f843-4aee-53b4-97c2-82782e951af5) and [other stores](https://www.copetti.org/writings/consoles/materials/book/). The proceeds support the improvement of current articles and the development of new ones.
For more information, please take a look at [here](https://www.copetti.org/writings/consoles/materials/book/).
* * *
Table of Contents
  1. [Supporting imagery](https://www.copetti.org/writings/consoles/nintendo-64#imagery)
  2. [A quick introduction](https://www.copetti.org/writings/consoles/nintendo-64#a-quick-introduction)
  3. [CPU](https://www.copetti.org/writings/consoles/nintendo-64#cpu)
    1. [Simplified memory access](https://www.copetti.org/writings/consoles/nintendo-64#simplified-memory-access)
    2. [No DMA controller?](https://www.copetti.org/writings/consoles/nintendo-64#no-dma-controller)
    3. [Memory design](https://www.copetti.org/writings/consoles/nintendo-64#memory-design)
      1. [Latency and speed](https://www.copetti.org/writings/consoles/nintendo-64#latency-and-speed)
      2. [Leaving room for improvement](https://www.copetti.org/writings/consoles/nintendo-64#leaving-room-for-improvement)
    4. [Memory management](https://www.copetti.org/writings/consoles/nintendo-64#memory-management)
  4. [Graphics](https://www.copetti.org/writings/consoles/nintendo-64#graphics)
    1. [Architecture](https://www.copetti.org/writings/consoles/nintendo-64#architecture)
      1. [Reality Signal Processor](https://www.copetti.org/writings/consoles/nintendo-64#tab-1-1-reality-signal-processor)
      2. [Reality Display Processor](https://www.copetti.org/writings/consoles/nintendo-64#tab-1-2-reality-display-processor)
      3. [Remaining steps](https://www.copetti.org/writings/consoles/nintendo-64#remaining-steps)
    2. [Quick demo](https://www.copetti.org/writings/consoles/nintendo-64#quick-demo)
      1. [Vertex Processing](https://www.copetti.org/writings/consoles/nintendo-64#tab-2-1-vertex-processing)
      2. [Pixel processing](https://www.copetti.org/writings/consoles/nintendo-64#tab-2-2-pixel-processing)
    3. [Designs](https://www.copetti.org/writings/consoles/nintendo-64#designs)
    4. [Modern visible surface determination](https://www.copetti.org/writings/consoles/nintendo-64#modern-visible-surface-determination)
    5. [Secrets and limitations](https://www.copetti.org/writings/consoles/nintendo-64#secrets-and-limitations)
      1. [Pipeline Stalls](https://www.copetti.org/writings/consoles/nintendo-64#tab-3-1-pipeline-stalls)
      2. [Texture memory](https://www.copetti.org/writings/consoles/nintendo-64#tab-3-2-texture-memory)
    6. [The universal video out](https://www.copetti.org/writings/consoles/nintendo-64#the-universal-video-out)
  5. [Audio](https://www.copetti.org/writings/consoles/nintendo-64#audio)
    1. [The repertoire](https://www.copetti.org/writings/consoles/nintendo-64#the-repertoire)
    2. [Secrets and limitations](https://www.copetti.org/writings/consoles/nintendo-64#secrets-and-limitations-1)
  6. [Operating System](https://www.copetti.org/writings/consoles/nintendo-64#operating-system)
    1. [Boot process](https://www.copetti.org/writings/consoles/nintendo-64#boot-process)
  7. [I/O](https://www.copetti.org/writings/consoles/nintendo-64#io)
    1. [Accessories](https://www.copetti.org/writings/consoles/nintendo-64#accessories)
  8. [Games](https://www.copetti.org/writings/consoles/nintendo-64#games)
    1. [Source Development Kit](https://www.copetti.org/writings/consoles/nintendo-64#source-development-kit)
    2. [The alternative medium](https://www.copetti.org/writings/consoles/nintendo-64#the-alternative-medium)
  9. [Anti-piracy / Region Lock](https://www.copetti.org/writings/consoles/nintendo-64#anti-piracy-region-lock)
    1. [Unused ports](https://www.copetti.org/writings/consoles/nintendo-64#unused-ports)
    2. [Emulation](https://www.copetti.org/writings/consoles/nintendo-64#emulation)
  10. [That’s all folks](https://www.copetti.org/writings/consoles/nintendo-64#thats-all-folks)
  11. [Copyright and permissions](https://www.copetti.org/writings/consoles/nintendo-64#referencing)
  12. [Sources / Keep Reading](https://www.copetti.org/writings/consoles/nintendo-64#sources)
  13. [Contributing](https://www.copetti.org/writings/consoles/nintendo-64#contributing)
  14. [Changelog](https://www.copetti.org/writings/consoles/nintendo-64#changelog)


* * *
## Supporting imagery
  * [Model](https://www.copetti.org/writings/consoles/nintendo-64#cover-model)
  * [Motherboard](https://www.copetti.org/writings/consoles/nintendo-64#cover-motherboard)
  * [Diagram](https://www.copetti.org/writings/consoles/nintendo-64#cover-diagram)


### Model
[![Model](https://www.copetti.org/images/consoles/nintendo64/international.9e449590112030a45a7b53a7625f2ef6691615ca5561fdd4bbc0fe75eb64742a.png)](https://www.copetti.org/images/consoles/nintendo64/international.9e449590112030a45a7b53a7625f2ef6691615ca5561fdd4bbc0fe75eb64742a.png)The Nintendo 64.  
Released on 23/06/1996 in Japan, 29/09/1996 in America and 01/03/1997 in Europe
### Motherboard
  * [Original](https://www.copetti.org/writings/consoles/nintendo-64#cover-motherboard-original)
  * [Marked](https://www.copetti.org/writings/consoles/nintendo-64#cover-motherboard-marked)

[![Motherboard](https://www.copetti.org/images/consoles/nintendo64/motherboard.ef74cf5b75936e8646de9e6e6ea8c2cce9529d2b9f4be87cec98b11494dd31c5.png)](https://www.copetti.org/images/consoles/nintendo64/motherboard.ef74cf5b75936e8646de9e6e6ea8c2cce9529d2b9f4be87cec98b11494dd31c5.png)Motherboard  
Showing revision 'NUS-CPU-03'.  
Later ones reduced the number of chips required for AV encoding.  
Disk Drive connector is found on the back[![Motherboard](https://www.copetti.org/images/consoles/nintendo64/motherboard_marked.f17f4e419a7d1548423c412182e72cac589eb3b7d4649e9cc3540590ab2872e8.png)](https://www.copetti.org/images/consoles/nintendo64/motherboard_marked.f17f4e419a7d1548423c412182e72cac589eb3b7d4649e9cc3540590ab2872e8.png)Motherboard with important parts labelled
### Diagram
[![Diagram](https://www.copetti.org/images/consoles/nintendo64/_diagrams/main.539378342bba0c6d07cfcab63c7624f66828872aa3e22dfe5f10762d43112f9d.png)](https://www.copetti.org/images/consoles/nintendo64/_diagrams/main.539378342bba0c6d07cfcab63c7624f66828872aa3e22dfe5f10762d43112f9d.png)Main architecture diagram
* * *
## A quick introduction
Nintendo’s goal was to give players the _best_ possible graphics. For this, it partnered with one of the biggest names in computer graphics to produce the _ultimate_ graphics chip.
The result was a sleek console for the family… and a 500-page manual for the developer.
Don’t worry, I promise this article won’t be _that_ long… Enjoy!
* * *
## CPU
The origins of the Nintendo 64’s main processor trace back to the **MIPS R4000** , [MIPS](https://www.copetti.org/writings/consoles/playstation/#tab-1-2-mips-and-sony)’ new avant-garde CPU. Released in 1991, the R4000’s most apparent novelty was the inclusion of **64-bit capabilities** , which resulted from widening the buses, registers and computation units to manipulate 64-bit values with efficiency. Developers, on the other hand, accessed these capabilities through the new **MIPS III** instruction set. All in all, the R4000 enabled new applications to manipulate larger chunks of data without consuming extra cycles.
For their next-generation console, Nintendo looked into bringing industrial hardware into the home. Unlike [Sony](https://www.copetti.org/writings/consoles/playstation/#cpu), who owned an array of in-house components and only needed a MIPS second-source, Nintendo formed a direct partnership with the owners of MIPS (and numerous graphics workstations) to co-design their entire ecosystem. That company was **Silicon Graphics Incorporated** (SGI).
Back at SGI’s headquarters, the R4000 was an expensive product (priced at around $400 [[1]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-r4000demo)), which made it unfeasible for a video game console. Still, Nintendo didn’t want to give up on their state-of-the-art ambitions, so they opted for a low-end variant called **R4300i** , which NEC was able to second-source.
[![Image](https://www.copetti.org/images/consoles/nintendo64/r4300i.a166682feb6855ad7e924a30abc4f0ba0cea3c42fd26a50b8de479a3bb6297ec_hu_c2e52ed36ec90679.png)](https://www.copetti.org/images/consoles/nintendo64/r4300i.a166682feb6855ad7e924a30abc4f0ba0cea3c42fd26a50b8de479a3bb6297ec.webp)The MIPS R4300i CPU (1994).
In the end, Nintendo and SGI settled on the **NEC VR4300** clocked at **93.75 MHz** [[2]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-anatomy). This is a binary-compatible version of the MIPS R4300i that features [[3]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-nec):
  * **Two modes of operation** :
    * **32-bit mode** : Traditional mode in which the CPU behaves as a MIPS II-compatible processor. There’s nothing special about this mode except that all new functions are locked out.
    * **64-bit mode** : ‘Native’ mode where all 64-bit extensions are available. It’s also binary-compatible with 32-bit applications.
  * **32 general-purpose registers** : These are 32 bits wide in 32-bit mode, and 64 bits wide in 64-bit mode.
  * The **MIPS III ISA** : A RISC instruction set that builds on MIPS II. It introduces new opcodes for computing 64-bit words (called ‘doublewords’). Finally, instructions are always **32-bit long** , regardless of mode.
    * It’s worth mentioning that, starting with MIPS II, [load delay slots](https://www.copetti.org/writings/consoles/playstation/#delay-galore) became optional. Instead, the hardware can automatically interlock/stall the pipeline to prevent data hazards. This is an interesting contradiction to [MIPS’ initials](https://www.copetti.org/writings/consoles/playstation/#a-core-philosophy)!
    * Weirdly, branch delay slots still persist, but there are new branch instructions that can discard the delay slot. Although these were removed in later revisions of the instruction set [[4]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-chen).
  * An internal **64-bit bus** connected to an **external 32-bit data bus** : While doublewords operations don’t degrade performance when operated internally, moving 64-bit data across the system incurs extra cycles.
    * This is one of the cutbacks of the R4300i variant (the R4000 features a full 64-bit data bus).
  * **32-bit address bus** : Capable of addressing up to 4 GB of physical memory.
  * **Five-stage pipeline** : Up to five instructions can be allocated for execution (a detailed explanation can be found in a [previous article](https://www.copetti.org/writings/consoles/sega-saturn/#cpu)).
  * **24 KB of L1 cache** : Partitioned into 16 KB for instructions and 8 KB for data.


The package also includes an internal **Floating-Point Unit** (FPU). The VR4300 designates it as a co-processor (CP1), however, the unit is fitted adjacent to the ALU and accessed solely via the ALU pipeline, meaning there’s no co-processing per se. On the other side, the FPU still houses a dedicated register file and speeds up operations involving 64-bit and 32-bit floating-point numbers. Finally, this unit adheres to the IEEE 754 standard.
### Simplified memory access
The way RAM is assembled follows the **Unified Memory Architecture** (UMA), wherein all available RAM is centralised in one place only, and any component requiring RAM access draws from this shared location. The unit arbitrating its access is, in this case, the graphics chip.
The reason for choosing this design comes down to **manufacturing costs**. At the same time, if not managed properly, it also increments access contention.
### No DMA controller?
As a consequence of the unified memory architecture, the CPU no longer has direct access to RAM. Thus, the graphics chip provides the required [Direct Memory Access](https://www.copetti.org/writings/consoles/playstation/#taking-over-the-cpu) (DMA) functionality as well.
### Memory design
Apart from the UMA, the structure of RAM is a little bit complicated, so I’ll try to keep it simple. Here it goes…
The system physically contains **4.5 MB of RAM** ; however, it’s connected using a **9-bit** data bus, where the 9th bit is reserved for the GPU (I explain more in the ‘Graphics’ section). As a consequence, every component except the GPU will only find **up to 4 MB**.
[![Image](https://www.copetti.org/images/consoles/nintendo64/_diagrams/memory.e3d3e85cf8b06b80e3351fc3d26f1019cc4288aab6110f2897920e43aaad30d8.png)](https://www.copetti.org/images/consoles/nintendo64/_diagrams/memory.e3d3e85cf8b06b80e3351fc3d26f1019cc4288aab6110f2897920e43aaad30d8.png)Memory layout of this system. I assume the CPU-RCP bus speed matches either the RCP’s clock speed or the CPU’s.
The type of RAM fitted to the board is called **Rambus DRAM** (RDRAM) [[5]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-memory). This was just another design that competed with ‘Synchronous DRAM’ (SDRAM) to become the next standard. RDRAM is connected using a fast **serial** architecture (where memory modules are chained in sequence), while SDRAM employs a slower **parallel connection** (wiring all modules directly to the memory controller). Each came with its own advantages and disadvantages, both technical and commercial. Nevertheless, it’s worth pointing out that although SDRAM ultimately triumphed, RDRAM continued to appear in later console generations, each introducing a new revision of the protocol.
Finally, the Nintendo 64 implemented the **Base RDRAM** variant [[6]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-rdram_brew) - the very first revision of the protocol.
#### Latency and speed
While RDRAM installations required less wiring and enjoyed greater clock speeds than SDRAM, access latency increased proportionally with the number of banks installed [[7]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-rdram). In the case of the Nintendo 64, the delay between initiating a memory transaction to finding the value in cache was significant - around **640 ns** [[8]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-beyondrsp). Engineers tried to offset this by applying a high clock speed of **250 MHz** (approximately 2.6 times faster than the CPU) to the memory banks. This way, Nintendo claimed that RDRAM could deliver high-speed data transfers of up to 500 MB/sec when reading or writing **consecutive** data [[9]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-dreamteam).
As a side note, Nintendo chose NEC’s uPD488170L memory banks for the N64’s motherboard [[10]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-beyondrdram). These chips implement a technology known as ‘Rambus Signaling Logic’ - an umbrella term used to promote many advancements, one of which doubles the transfer rate [[11]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-data). This may explain why some sources cite the ‘effective’ memory rate as 500 MHz.
#### Leaving room for improvement
Interestingly, the amount of available RAM on this console **can be expanded** by installing the **Expansion Pak** accessory - a peculiar box that adds another **4.5 MB**. While this accessory remained optional for some games (and the majority didn’t make use of it), certain titles such as _Donkey Kong 64_ and _The Legend of Zelda: Majora’s Mask_ were designed with the expansion as a requirement, and would display an error screen if it was not present.
  * [Expansion](https://www.copetti.org/writings/consoles/nintendo-64#nestedtab-1-1-expansion)
  * [Placeholder](https://www.copetti.org/writings/consoles/nintendo-64#nestedtab-1-2-placeholder)

[![Image](https://www.copetti.org/images/consoles/nintendo64/expansion_pak.a13f39147a2b35c93b1a5cd5061841317a3988a480527337a73c818bb5854f52.png)](https://www.copetti.org/images/consoles/nintendo64/expansion_pak.a13f39147a2b35c93b1a5cd5061841317a3988a480527337a73c818bb5854f52.png)The Expansion Pak [[12]](https://www.copetti.org/writings/consoles/nintendo-64#bib:photography-amos), an optional accessory sold separately (sometimes bundled with the game that required it).[![Image](https://www.copetti.org/images/consoles/nintendo64/jumper_pak.3c9133ee2e44819ae4d027e9e165a443aa90f34eba5d36f2ec5640debe7069a9.png)](https://www.copetti.org/images/consoles/nintendo64/jumper_pak.3c9133ee2e44819ae4d027e9e165a443aa90f34eba5d36f2ec5640debe7069a9.png)The Jumper Pak [[13]](https://www.copetti.org/writings/consoles/nintendo-64#bib:photography-amos). In the absence of the Expansion Pak, this must be present to terminate the RDRAM bus.
Due to its end-to-end design, RDRAM must be **properly terminated** ; otherwise, signals would bounce back and forth along the bus (a common phenomenon known as **reflection**). Rambus mitigated this by requiring PC users to install memory modules in pairs and to fill all unused slots with ‘Continuity RIMM’ (CRIMM) modules, which acted as terminators. For this console, however, Nintendo shipped a terminator called **Jumper Pak** , which came fitted in place of the Expansion Pak. The Jumper Pak housed only enough capacitors and resistors to match the bus’s impedance [[14]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-jp_reversed), thereby reducing reflection. It also served to close the loop in the serial chain [[15]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-rdram_brew).
Now, you may ask, what would happen if you switched on the console without any _Pak_ installed? Well, the onboard memory chips won’t be functional, so the boot sequence will fail and nothing will come out of the video signal.
### Memory management
The VR4300 includes another coprocessor known as the **System Control Coprocessor** (CP0), which is composed of a **Memory Management Unit** (MMU) and a **Translation Lookaside Buffer** (TLB). The MMU governs how memory is organised and cached.
Although the CPU is capable of addressing up to 4 GB worth of memory, the Nintendo 64 contains far less, even after considering [memory-mapped I/O](https://www.copetti.org/writings/consoles/nes/#memory). For that reason, the MMU provides efficient uses for addressing limited memory, including a **virtual memory map** in which physical memory is mirrored multiple times. Consequently, memory locations are treated as **virtual addresses** (as opposed to ‘physical addresses’). Furthermore, this layout is enhanced by the TLB, which enables developers to define custom memory maps in some mirrors without adding (significant) performance penalties.
At first glance, all of this may seem redundant. However, each mirror (called **segment**) is connected to distinct circuitry (e.g. L1 cache, physical RAM, or TLB-mapped regions), allowing developers to optimise usage by selecting the most appropriate segment depending on the needs [[16]](https://www.copetti.org/writings/consoles/nintendo-64#bib:audio-memory_map).
Some segments were designed to distinguish between ‘kernel’ and ‘user’ locations for security purposes. Nevertheless, the N64 always operates in ‘kernel’ mode, making the ‘non-TLB kernel cached’ segment (called ‘KSEG0’) the most commonly used for games.
Finally, the MMU can also work in 64-bit mode, where memory addresses are 40 bits long. This extends the virtual address space to approximately 1 TB worth of addresses… but I don’t think the Nintendo 64 will ever take advantage of this!
* * *
## Graphics
What you see on screen is produced by a large chip designed by Silicon Graphics called **Reality Co-Processor** (RCP), which runs at **62.5 MHz** [[17]](https://www.copetti.org/writings/consoles/nintendo-64#bib:graphics-rcp2010). This package contains _a lot_ of circuitry, so don’t worry if you find it difficult to follow - the graphics subsystem has a very complex architecture!
This design is based on the philosophy that the GPU should not be a ‘mere’ rasteriser like the [competition](https://www.copetti.org/writings/consoles/playstation/#graphics). Instead, it should also be capable of **accelerating geometry calculations** (offloading work from the CPU), and for that, more circuitry is needed.
### Architecture
The Reality Co-Processor is divided into three main modules, two of which are dedicated to graphics processing:
  * [Reality Signal Processor](https://www.copetti.org/writings/consoles/nintendo-64#tab-1-1-reality-signal-processor)
  * [Reality Display Processor](https://www.copetti.org/writings/consoles/nintendo-64#tab-1-2-reality-display-processor)


#### Reality Signal Processor
[![Image](https://www.copetti.org/images/consoles/nintendo64/_diagrams/rsp.78b56afee1c8e869b864c95e722374909cbf8c10536255d06f94de61faadd2fe.png)](https://www.copetti.org/images/consoles/nintendo64/_diagrams/rsp.78b56afee1c8e869b864c95e722374909cbf8c10536255d06f94de61faadd2fe.png)Architecture of the Reality Signal Processor (RSP).
Also known as **RSP** , the Reality Signal Processor is a CPU package composed of [[18]](https://www.copetti.org/writings/consoles/nintendo-64#bib:graphics-rsp):
  * The **Scalar Unit** : Another cut-down derivative of the MIPS R4000. This time, it only implements a subset of the MIPS III ISA, and therefore lacks many general-purpose functions, including interrupts, the 64-bit extension, multiplication, and division.
  * The **Vector Unit** : A co-processor that performs vector operations with **32 128-bit registers**. Each register is _sliced_ into eight parts to operate eight 16-bit vectors at once (similar to SIMD instructions in conventional CPUs). As you can see, this component does the heavy lifting for the Scalar Unit (while also working concurrently).
  * The **System Control** : Another co-processor that provides DMA functionality and controls its neighbouring module, the RDP (explained in the next section).


To operate the RSP, the CPU stores a series of commands called **Display list** in RAM, along with the data to be manipulated. The RSP then reads the list and performs the required operations on it. Available functions include geometry transformations (such as perspective projection), clipping, and lighting.
This may seem straightforward, but how does it perform these operations? Well, here’s the interesting part: unlike its competitors (the [PlayStation](https://www.copetti.org/writings/consoles/playstation/) and [Sega Saturn](https://www.copetti.org/writings/consoles/sega-saturn/)), **the geometry engine is not hard-wired**. Instead, the RSP contains some memory (4 KB for instructions and 4 KB for data) to store **microcode** [[19]](https://www.copetti.org/writings/consoles/nintendo-64#bib:graphics-rcp2010): A small program, with no more than 1000 instructions, that **implements the graphics pipeline**. In other words, it tells the Scalar Unit how to process the graphics data. The microcode is fed by the main CPU at runtime.
Nintendo provided multiple microcodes to choose from and, similar to the [SNES’ background modes](https://www.copetti.org/writings/consoles/super-nintendo/#graphics), each one balances system resources differently [[20]](https://www.copetti.org/writings/consoles/nintendo-64#bib:audio_video-microcodes).
The resulting data is transmitted either via a dedicated bus called **XBUS** or through main RAM. Over the console’s lifetime, this choice fluctuated due to memory constraints: the XBUS path was faster but required additional buffers in the RSP’s internal memory to hold (and transfer) the new data. To give you an idea, early microcode programs like `Fast3D` offered both options. However, the later and faster `F3DEX` focused entirely on main RAM. Finally, its successor, `F3DEX2`, reintroduced XBUS support after sorting out memory usage.
« Previous [Next »](https://www.copetti.org/writings/consoles/nintendo-64#tab-1-2-reality-display-processor)
#### Reality Display Processor
[![Image](https://www.copetti.org/images/consoles/nintendo64/_diagrams/rdp.8681ae23dc4324b42e4269ae096ddecfcc948ed8e7fc3ded2fdbd5d78d1693f9.png)](https://www.copetti.org/images/consoles/nintendo64/_diagrams/rdp.8681ae23dc4324b42e4269ae096ddecfcc948ed8e7fc3ded2fdbd5d78d1693f9.png)Architecture of the Reality Display Processor (RDP).
After the RSP finishes processing the data, it will start sending **rasterisation commands** to the next module - the **Reality Display Processor** (RDP) - to draw the frame.
The RDP is another processor (this time with fixed functionality) that includes multiple engines to rasterise vectors, map textures onto polygons, mix colours, and compose the new frame.
It can process either **triangles** or **rectangles** as primitives, the latter being useful for drawing sprites. The RDP’s rasterisation pipeline contains the following blocks [[21]](https://www.copetti.org/writings/consoles/nintendo-64#bib:graphics-rdp):
  * A **Rasteriser** : Converts primitives (made of vertices) into pixels.
  * A **Texture Unit** : Processes textures using **4 KB of dedicated memory** (called ‘TMEM’), allowing up to eight tiles to be used for texturing. It can perform the following operations on them:
    * **Bilinear filtering** : Maps the selected 2D texture onto the 3D shape and smooths it to avoid pixelated areas (caused by oversampling).
      * A ‘complete’ filter would require four points to carry out the interpolation; however, this console uses only three (**triangular interpolation**), resulting in some anomalies. Thus, certain textures have to be ‘adapted’ beforehand.
    * **Mip-Mapping** : Automatically selects a scaled-down version of the texture depending on its **level of detail**. This avoids computing large textures that are seen far from the camera and prevents aliasing (the result of undersampling).
      * If enabled, the RDP maps textures using **trilinear filtering** instead. This new algorithm also interpolates between mipmaps to soften abrupt changes between the levels of detail.
    * **Perspective correction** : The chosen algorithm for mapping textures onto triangles. Unlike [other inverse-mapping algorithms](https://www.copetti.org/writings/consoles/playstation/#graphics), this one accounts for the depth value of each primitive, achieving more faithful results.
  * A **Colour Combiner** : Mixes and interpolates multiple layers of colours. As the _next-generation_ [color math unit](https://www.copetti.org/writings/consoles/super-nintendo/#more-colour-magic), it performs addition, multiplication, and subtraction of colour values.
  * A **Blender** : Mixes pixels with the current frame buffer to apply translucency, anti-aliasing, fog, and dithering. It also performs z-buffering, which I explain more later on.
  * A **Memory Interface** : Used by the previous blocks to read from and write to the current frame buffer in RAM and/or populate TMEM.


The RDP provides **four operating modes** , each of which combines these blocks differently to optimise specific tasks.
Since this module constantly updates the frame buffer, it interacts with main RAM in a unique way. Remember the unusual 9-bit ? The ninth bit is used as metadata for frame buffer-related calculations (i.e. z-buffering and antialiasing) and is only understood by the Memory Interface.
[« Previous](https://www.copetti.org/writings/consoles/nintendo-64#tab-1-1-reality-signal-processor) Next »
#### Remaining steps
The resulting frame must be sent to the **Video Encoder** to be displayed on-screen. **DMA** and the **Video Interface** component are essential to accomplish this.
The theoretical maximum capabilities of the output frame are a **24-bit colour depth** (16.8 million colours) and a resolution of **640x480 pixels** (or 720x576 in the PAL region) [[22]](https://www.copetti.org/writings/consoles/nintendo-64#bib:graphics-video_interface). I mention ‘theoretical’ because using the maximum capabilities can be resource-hungry, so programmers often opt for lower specifications to free up enough resources for other services.
### Quick demo
Let’s put all the previous explanations into perspective, for that, I will use Nintendo’s _Super Mario 64_ as a case study to show, in a nutshell, how a basic frame is composed. Just bear in mind that, in practice, however, games may employ additional buffers to compose richer frames.
  * [Vertex Processing](https://www.copetti.org/writings/consoles/nintendo-64#tab-2-1-vertex-processing)
  * [Pixel processing](https://www.copetti.org/writings/consoles/nintendo-64#tab-2-2-pixel-processing)


#### Vertex Processing
[![Image](https://www.copetti.org/images/consoles/nintendo64/mario/wireframe.1850a123f94e45ea78b5ec2093420422577a90abbf6bf252fd7fdeaea861749e.jpg)](https://www.copetti.org/images/consoles/nintendo64/mario/wireframe.1850a123f94e45ea78b5ec2093420422577a90abbf6bf252fd7fdeaea861749e.jpg)Primitive view of our scene. In order to save polygons, some characters are modelled using sprites (quads)
Initially, materials such as 3D models are located in the cartridge ROM. However, to keep a steady bandwidth, we need to copy them to RAM first. In some cases, the data is pre-compressed within the cartridge, requiring the CPU to decompress it before use.
Once that’s done, it’s time to build a scene using our models. The CPU _could_ carry out the entire graphics pipeline by itself, but that _takes ages_ , so many tasks are offloaded to the RCP. The CPU will instead send orders to the RCP, this is done by carrying out these steps:
  1. Compose the **Display Lists** that contain the operations to be executed by the RSP, and store them in RAM. The structure of Display Lists is dictated by the choice of microcode [[23]](https://www.copetti.org/writings/consoles/nintendo-64#bib:graphics-rcp_structures).
  2. Point the RSP to the location of the Display Lists.
  3. Upload the chosen microcode to the RSP, kickstarting the Scalar Unit.


Afterwards, the RSP begins working on the first batch of tasks. The result is then passed to the RDP in the form of rasterisation commands.
« Previous [Next »](https://www.copetti.org/writings/consoles/nintendo-64#tab-2-2-pixel-processing)
#### Pixel processing
[![Image](https://www.copetti.org/images/consoles/nintendo64/mario/result.b2752516dc322bd5c2df330b15e39486e958923a863f427a7e30350683168d97.png)](https://www.copetti.org/images/consoles/nintendo64/mario/result.b2752516dc322bd5c2df330b15e39486e958923a863f427a7e30350683168d97.png)Rendered frame (_Tada!_).
So far, we’ve managed to process our data and apply some effects, but we still need to:
  * Rasterise vectors, apply textures and other effects.
  * Display the frame buffer.


As you might expect, these tasks are performed by the RDP. Additionally, to make this work, textures must be transferred into the 4 KB of Texture Memory using DMA.
Unlike the previous processor, the RDP’s pipeline is fixed, but we can select the optimal mode of operation based on workload, performance and specific tasks needed. For instance, commanding the RDP to render a single texture is faster than combining two.
Once the RDP finishes processing the data, it writes the final bitmap to the frame buffer area in RAM. Afterwards, the CPU must transfer the new frame to the **Video Interface** (VI), preferably using DMA. The VI, in turn, sends it to the **Video Encoder** for display [[24]](https://www.copetti.org/writings/consoles/nintendo-64#bib:graphics-video_interface).
[« Previous](https://www.copetti.org/writings/consoles/nintendo-64#tab-2-1-vertex-processing) Next »
### Designs
Here are some examples of classic 2D characters from the [Super Nintendo](https://www.copetti.org/writings/consoles/super-nintendo/) that were redesigned for the 3D era. Notice the texture detail when compared with models from other consoles of the same generation.
Wireframe | Surface | Textured  
---|---|---  
![3D model](https://www.copetti.org/images/consoles/models/link_ocarina_64.77a5ce05bd3cecace60dc8025caa3b5640305d2e8c7fbc40d8c318c4fdcc7da8.png)  
Tap to enable interaction  
The Legend of Zelda: Ocarina of Time (1998).  
704 triangles. Wireframe | Surface | Textured  
---|---|---  
![3D model](https://www.copetti.org/images/consoles/models/kirby_cristals_64.489d420698154a28ff960f44945640b1f5facb8388d9cc4887763530e64a8ce5.png)  
Tap to enable interaction  
Kirby 64: The Crystal Shards (2000).  
516 triangles.
### Modern visible surface determination
If you’ve read about the preceding consoles, you’ll have come across the never-ending problem of [visibility of surfaces](https://www.copetti.org/writings/consoles/sega-saturn/#an-introduction-to-the-visibility-problem), and by now may think polygon sorting is the only way out of this. Well, for the first time in this series, the graphics chip features a hardware-based approach called **Z-buffering**. In a nutshell, the RDP allocates an extra buffer (called **Z-buffer**) in memory. This has the same dimensions as a frame buffer, but instead of storing RGB values, each entry contains the depth (Z-value) of the nearest pixel relative to the camera.
After the RDP rasterises the vectors, the z-value of the new pixels are compared against the corresponding value in the z-buffer. If the new pixel has a smaller z-value, it means the new pixel is positioned in front of the previous one, so it is applied to the frame buffer and the z-buffer is also updated. Otherwise, the pixel is discarded.
Overall, this is a hugely welcome addition: programmers no longer need to worry about implementing [software-based](https://www.copetti.org/writings/consoles/playstation/#tab-3-2-visibility-approach) polygon sorting methods, which drain significant CPU resources. However, the z-buffer does not prevent feeding unnecessary geometry (whether discarded or overdrawn, both wasting resources). For this, game engines may choose to include an **occlusion culling** algorithm to discard unseen geometry as early as possible.
### Secrets and limitations
SGI clearly invested a lot of technology into this system. Nevertheless, the Nintendo 64 was a console intended for the home market and, as such, needed to keep its cost down. Some tough compromises resulted in difficult challenges for programmers:
  * [Pipeline Stalls](https://www.copetti.org/writings/consoles/nintendo-64#tab-3-1-pipeline-stalls)
  * [Texture memory](https://www.copetti.org/writings/consoles/nintendo-64#tab-3-2-texture-memory)


#### Pipeline Stalls
Due to the large number of components and operations in the graphics pipeline, the RCP became highly susceptible to **stalls** : an undesirable situation in which sub-components remain idle for considerable periods, as the required data is delayed at the back of the pipeline.
This invariably results in performance degradation, and it is the programmer’s job to avoid it. Although, to alleviate things, MIPS-based CPUs such as the Scalar Unit implement a mechanism called **bypassing** , which enables similar instructions to execute at a faster rate by bypassing some execution stages that can be skipped [[25]](https://www.copetti.org/writings/consoles/nintendo-64#bib:cpu-nec).
For example, if the CPU has to compute sequential `ADD` instructions that are dependent on each other, there’s no need to write the result back to a register and then read it again after each operation. Instead, the CPU can forward the values within the datapath and perform the write-back only after the last `ADD` has been completed.
« Previous [Next »](https://www.copetti.org/writings/consoles/nintendo-64#tab-3-2-texture-memory)
#### Texture memory
The RDP relies on 4 KB of Texture Memory (TMEM) as a single source for loading textures. Unfortunately, 4 KB proved to be insufficient for high-resolution textures. Furthermore, when mipmapping is activated, the available memory is reduced to half.
As a result, some games used solid colours with Gouraud shading (_Super Mario 64_ being a notable example), while others relied on pre-computed textures (particularly, where multiple layers had to be combined).
[« Previous](https://www.copetti.org/writings/consoles/nintendo-64#tab-3-1-pipeline-stalls) Next »
### The universal video out
Nintendo carried on using the ‘universal’ [Multi Out](https://www.copetti.org/writings/consoles/super-nintendo/#a-convenient-video-out) port from its predecessor, bad news is that it **no longer carries the RGB signal!** It looks to me like another cost-saving measure, given that RGB wasn’t widely adopted in the previous console.
The good news is that, on early revisions of the Nintendo 64, the three RGB lines can still be restored by soldering some cables and fitting an inexpensive signal amplifier. This is possible because the video Digital-to-Analogue Converter (DAC) still transmits an RGB signal to the video encoder [[26]](https://www.copetti.org/writings/consoles/nintendo-64#bib:graphics-video_dac). However, later motherboard revisions combined both chips, so the only remaining option is to bypass the video DAC and encoder altogether with custom circuitry that exposes RGB signals.
* * *
## Audio
Before we go into the details, let’s define the two endpoints of the N64’s audio subsystem:
  * Our starting point is the cartridge ROM, which contains data that only the CPU can interpret.
  * The ending point is the **Digital-to-Analog Converter** (DAC), which only understands _waveform_ data [[27]](https://www.copetti.org/writings/consoles/nintendo-64#bib:audio-programming).


Now, how do we connect both ends? Consoles normally include a dedicated audio chip that does the work for us. Unfortunately, the Nintendo 64 **doesn’t have a dedicated chip** , so this task is distributed across these components:
  * The **main CPU** : Transfers the audio data from the game’s ROM to RAM, then composes **Audio Lists** to be handled by the RSP.
  * The **RSP** : Using additional microcode, it interprets the audio lists previously stored in RAM and performs the required operations on the audio data, which can include:
    * Decompressing **ADPCM samples** and applying effects.
    * Sequencing and mixing **MIDI data** using **audio banks** stored in RAM.


The resulting data is, as expected, waveform data. This is then sent to the **Audio Interface** (AI) block, which transfers it to the digital-to-analogue converter [[28]](https://www.copetti.org/writings/consoles/nintendo-64#bib:audio-audio_interface). Being a stereo system, the resulting waveform contains two channels, each with 16-bit resolution.
[![Image](https://www.copetti.org/images/consoles/nintendo64/_diagrams/audio.b5d3afa84223dc0f9b4702e6505440ed6aedcd09ef97ecf41ec1cad071638b79.png)](https://www.copetti.org/images/consoles/nintendo64/_diagrams/audio.b5d3afa84223dc0f9b4702e6505440ed6aedcd09ef97ecf41ec1cad071638b79.png)Overview of how the audio pipeline is commonly implemented.
### The repertoire
Time to check out the soundtracks made for the N64. There are too many (good ones) to mention in this article, so here are some that caught my attention:
No support for video.The Legend of Zelda: Majora’s Mask (2000).  
The music of this game is tied to its daunted atmosphere. No support for video.Bomberman Hero (1998).  
This game has a nice and unique house-based soundtrack.
### Secrets and limitations
Because of this design, the constraints are dictated by the overall workload:
  * The sampling rate can be up to **44.1 kHz** , but using the top rate steals too many CPU cycles.
  * There’s no strict limit on the number of channels; it all depends on how much the RSP is capable of mixing (often around 16-24 channels when processing ADPCM, or approximately 100 with PCM).
  * Memory is another concern. While competitors relied on larger media (i.e. CD-ROM) and dedicated audio memory, Nintendo 64 cartridges hold much less data (let alone music data) and must share main memory with other components.


For these reasons, players may notice that N64 ports feature lower-quality music or repeated scores. A common workaround is to implement a music sequencer that generates samples at runtime using a pre-populated set of sounds (resembling MIDI music).
* * *
## Operating System
Similar to the PS1 and Saturn, N64 games are written for bare metal. However, there are no BIOS routines available to simplify hardware operations. As a substitute, **games embed a small operating system** that provides a fair amount of abstraction to efficiently manage the CPU, GPU, and I/O.
This is not the conventional _desktop OS_ that we may imagine at first, it’s just a microkernel with the smallest possible footprint that offers the following functionality [[29]](https://www.copetti.org/writings/consoles/nintendo-64#bib:operating_system-schd):
  * Multithreading using message passing.
  * Scheduling and preemption.
  * Simplified register and I/O access.


All in all, these functions are critical for coordinating audio, video, and game logic tasks - all of which need to work concurrently - in an efficient manner.
The kernel is automatically embedded when using Nintendo’s libraries. Additionally, if programmers decide not to include part of the library set, the corresponding portion of the kernel is stripped to avoid wasting cartridge space.
### Boot process
Unlike previous cartridge-based systems, the Nintendo 64 follows a sophisticated boot process to prepare all of its hardware before the actual game runs. This process begins as soon as the user powers on the console and is very similar to its CD-based contemporaries bundling a [BIOS](https://www.copetti.org/writings/consoles/playstation/#operating-system) or [IPL](https://www.copetti.org/writings/consoles/sega-saturn/#operating-system).
These routines are also referred to as **Initial Program Loader** (IPL) and work as follows [[30]](https://www.copetti.org/writings/consoles/nintendo-64#bib:operating_system-ipl) [[31]](https://www.copetti.org/writings/consoles/nintendo-64#bib:operating_system-ipl_decomp):
  1. The user turns on the console.
  2. The **PIF-NUS** (a separate chip on the motherboard) subdues the main CPU into an infinite reset until it validates the CIC chip found in the game cartridge.
     * The PIF-NUS and the CIC chip are explained further in the I/O and anti-piracy sections, respectively.
  3. If the verification process finishes successfully, the CPU starts execution at `0xBFC00000`. This address points to an **internal ROM** within PIF-NUS, specifically the first boot stage called **IPL1**.
  4. IPL1 initialises part of the hardware (CPU registers, the parallel interface, and the RCP), then copies the next stage (**IPL2**) from the internal ROM to the RSP’s memory for faster execution. It then redirects execution there.
  5. IPL2 copies the first four bytes of the game ROM into the RSP’s memory. This is used to adjust the ROM bus timings. Afterwards, it copies another 4 KB of the ROM header and sends a checksum of it to the PIF-NUS, which verifies the checksum using the cartridge’s CIC chip. If the verification fails, the PIF-NUS interrupts the CPU indefinitely. Otherwise, the CPU continues execution on those 4 KB, which contain the next boot stage, called **IPL3**.
  6. IPL3 initialises RDRAM, the CPU cache, and the Expansion Pak (if present). Afterwards, it copies 1 MB of game ROM into RDRAM, computes its checksum, and compares it against a precomputed value stored in the ROM header. Finally, the CPU jumps to the game code in RDRAM.


As IPL3 resides within the game cartridge, not every game includes the same code. Additionally, the IPL3 checksum stored in the CIC is hardcoded [[32]](https://www.copetti.org/writings/consoles/nintendo-64#bib:operating_system-ipl). Thus, the CIC chip and IPL3 variants found in the cartridge are bound together and cannot be swapped with different models.
* * *
## I/O
As you know by now, I/O is not directly connected to the CPU, so the RCP’s third module - which I haven’t mentioned until now - serves as an **I/O interface**. This block handles communication with the CPU, controllers, game cartridge, and audio/video DACs.
### Accessories
In addition to its unorthodox shape, the Nintendo 64 controller includes a connector for plugging in accessories. Notable commercial examples include:
  * The **Controller Pak** : A storage medium, similar to Sony’s [Memory Card](https://www.copetti.org/writings/consoles/playstation/#front-ports), used to store save game data and share it across consoles.
  * The **Rumble Pak** : Contains a small motor that provides haptic feedback, useful for ‘immersing’ the player in supported games.
  * The **Transfer Pak** : Provides a slot to connect a Game Boy or Game Boy Color cartridge ([Game Pak](https://www.copetti.org/writings/consoles/game-boy/#games)). This enabled the possibility to run Game Boy games with the help of an emulator, and/or transfer its content.


  * [Controller](https://www.copetti.org/writings/consoles/nintendo-64#nestedtab-2-1-controller)
  * [Rumble](https://www.copetti.org/writings/consoles/nintendo-64#nestedtab-2-2-rumble)
  * [Transfer](https://www.copetti.org/writings/consoles/nintendo-64#nestedtab-2-3-transfer)

[![Image](https://www.copetti.org/images/consoles/nintendo64/accessories/controller_pak.57bf45296a04b011b9bf1ef070cd1dd091a804c6a6fd61123bcbd048395a8c73_hu_91b258e7da73c2be.png)](https://www.copetti.org/images/consoles/nintendo64/accessories/controller_pak.57bf45296a04b011b9bf1ef070cd1dd091a804c6a6fd61123bcbd048395a8c73.webp)The Controller Pak [[33]](https://www.copetti.org/writings/consoles/nintendo-64#bib:photography-amos).[![Image](https://www.copetti.org/images/consoles/nintendo64/accessories/rumble_pak.cf207e1cf6c8fe2a0b0601ab45a65e0fe5f158177d0964195387d0b4d9cb927d_hu_eb00a34559cb744e.png)](https://www.copetti.org/images/consoles/nintendo64/accessories/rumble_pak.cf207e1cf6c8fe2a0b0601ab45a65e0fe5f158177d0964195387d0b4d9cb927d.webp)The Rumble Pak [[34]](https://www.copetti.org/writings/consoles/nintendo-64#bib:photography-amos).[![Image](https://www.copetti.org/images/consoles/nintendo64/accessories/transfer_pak.cd1a8f12e99bef69f9c19ac22b85a4e9a8652b676e429329c822f064268de949_hu_3f5cc80e01735ab7.png)](https://www.copetti.org/images/consoles/nintendo64/accessories/transfer_pak.cd1a8f12e99bef69f9c19ac22b85a4e9a8652b676e429329c822f064268de949.webp)The Transfer Pak [[35]](https://www.copetti.org/writings/consoles/nintendo-64#bib:photography-amos).
All accessories connected to the controller are managed by the **PIF-NUS** , an obscure block that also handles security. The RCP communicates to the PIF using a **serial bus** [[36]](https://www.copetti.org/writings/consoles/nintendo-64#bib:io-serial_interface).
* * *
## Games
Nintendo held on to the cartridge medium for storage instead of adopting optical discs. As a consequence, games enjoyed higher bandwidths (an average of 5 MB/sec) while also being more expensive to manufacture. The largest cartridge found in the market had a capacity of 64 MB.
Inside cartridges, manufacturers often included extra memory (in the form of **EEPROM** , **flash** , or **SRAM** backed by battery) to hold save data. However, this became less essential, as certain accessories (like the Controller Pak) provided alternative storage.
Cartridges interface with the RCP using a dedicated 16-bit bus known as the **Parallel Bus** (PBUS) or ‘Parallel Interface’ (PI) [[37]](https://www.copetti.org/writings/consoles/nintendo-64#bib:games-peripheral_interface).
### Source Development Kit
In general, development was mainly done in **C** and **assembly** , the latter was often required to achieve better performance.
While we’ve seen this system supports 64-bit operations, the new instructions were rarely used since, in practice, 32-bit instructions happened to execute faster (given that the R4300i/VR4300 comes with a 32-bit data bus).
The libraries in the official SDK feature several layers of abstractions to command the RCP. For example, C structs like the **Graphics Binary Interface** (GBI) were designed to facilitate the assembly of Display lists [[38]](https://www.copetti.org/writings/consoles/nintendo-64#bib:games-gbi). The same applies to audio functions, its struct was called **Audio Binary Interface** (ABI).
In terms of microcode development, Nintendo provided a set of prewritten microcode programs to choose from. However, if developers wanted to customise them, that would indeed be a challenging task: the Scalar Unit instruction set wasn’t initially documented. Later on, however, Nintendo and SGI changed their stance and released some documentation and tools for microcode programming [[39]](https://www.copetti.org/writings/consoles/nintendo-64#bib:games-gbi).
[![Image](https://www.copetti.org/images/consoles/nintendo64/sgi_indy.167ee74d9c40297c33d79b1ef098d0ea3dfb2daa0715c491fa1306ac7d098e7b_hu_d42e8c8b32238043.png)](https://www.copetti.org/images/consoles/nintendo64/sgi_indy.167ee74d9c40297c33d79b1ef098d0ea3dfb2daa0715c491fa1306ac7d098e7b.webp)An SGI Indy I came across at The Centre for Computing History (Cambridge, UK) when I visited in August 2024. By comparison, this computer houses a MIPS R4400 CPU, an improved successor of the R4000 (all in all, miles ahead of the VR4300).
Hardware used for development included workstations supplied by SGI [[40]](https://www.copetti.org/writings/consoles/nintendo-64#bib:games-devkit), such as **Indy** machines equipped with an extra daughterboard called **U64**. This board contained the hardware and I/O of the retail console. Development tools were supplied for Windows-based computers as well [[41]](https://www.copetti.org/writings/consoles/nintendo-64#bib:games-u64).
Furthermore, there were third-party tools such as custom cartridges housing a long ribbon cable that connected to the workstation. These cartridges fitted in a retail Nintendo 64 but incorporated internal circuitry to redirect ‘read’ requests from the console to the workstation’s RAM. The deployment and debugging process involved transferring a copy of the game into RAM so that, upon powering the console, it would start reading from there.
### The alternative medium
Interestingly, the PBUS branches out to a secondary connector located on the underside of the Nintendo 64’s motherboard. This was intended for the **Nintendo 64 Disk Drive** (64DD), a peripheral that worked as an ‘extra floor’ beneath the console, housing a proprietary magnetic disk reader. The disks offered up to 64 MB of storage capacity.
Although the 64DD was only released in Japan, it opened the door to an alternative (and cheaper) medium for distributing games.
  * [Module](https://www.copetti.org/writings/consoles/nintendo-64#nestedtab-3-1-module)
  * [Attached](https://www.copetti.org/writings/consoles/nintendo-64#nestedtab-3-2-attached)

[![Image](https://www.copetti.org/images/consoles/nintendo64/64dd/module.74e356953f7787e8c2d280401107996d72373095268e3b39dc5d111590eda21b.png)](https://www.copetti.org/images/consoles/nintendo64/64dd/module.74e356953f7787e8c2d280401107996d72373095268e3b39dc5d111590eda21b.png)The Nintendo 64 Disk Drive [[42]](https://www.copetti.org/writings/consoles/nintendo-64#bib:photography-amos).  
Released on 01/12/1999 in Japan.[![Image](https://www.copetti.org/images/consoles/nintendo64/64dd/attached.76eb06e999484abb5a3654a14a3e3b34d800481745d1131ea6ddf228a885da71.png)](https://www.copetti.org/images/consoles/nintendo64/64dd/attached.76eb06e999484abb5a3654a14a3e3b34d800481745d1131ea6ddf228a885da71.png)The 64DD attached to the console [[43]](https://www.copetti.org/writings/consoles/nintendo-64#bib:photography-amos).
The magnetic medium used by the 64DD is slower than cartridges, with transfer speeds of up to 1 MB/sec - but still faster than 4x CD-ROM readers. The disks are double-sided and operate using **Constant Angular Velocity** (CAV), like the later [miniDVD](https://www.copetti.org/writings/consoles/gamecube/#medium). The smallest readable area is called a _block_ and corresponds to half of a concentric circle on the disk surface.
Notably, the reader **doesn’t include buffer memory** , so data is streamed directly into RDRAM for execution. To accommodate the increased memory demands, Nintendo bundled the RAM Expansion Pak with the 64DD. In doing so, it also standardised the extended RAM space, ensuring that all 64DD games could reliably take advantage of the additional memory.
Furthermore, portions of the disk are rewritable to enable save storage. The amount of writable space varies depending on the disk type (Nintendo offered seven types).
On the software side, game data is structured with a filesystem called ‘Multi File System’ (MFS) provided by Nintendo with their SDK [[44]](https://www.copetti.org/writings/consoles/nintendo-64#bib:games-rr_sdk). Games could access disk data either through the filesystem or via direct block-level access.
The Disk Drive also houses an internal ROM, known as ‘DDROM’, which stores code executed by the N64 during boot. This code bootstraps the disk and shows the splash animation, effectively adding a new IPL stage on top of the traditional boot process. The ROM also stores fonts (Latin and Kanji) and some sounds.
* * *
## Anti-piracy / Region Lock
The anti-piracy system is a continuation of the [Super Nintendo’s CIC](https://www.copetti.org/writings/consoles/super-nintendo/#anti-piracy--region-lock) model. As you know, earlier bootleg detection and region locking were enforced by the CIC chip (which was present in every _authorised_ game cartridge) [[45]](https://www.copetti.org/writings/consoles/nintendo-64#bib:anti_piracy-cic). The Nintendo 64 enhanced this system by assigning specific CIC chip variants to individual games, ensuring that each cartridge was not a counterfeit or contained a CIC clone.
To enforce this, the PIF-NUS conducts checksum verifications both at the startup and during gameplay to supervise the current CIC installed on the cartridge.
If the PIF determines the current cartridge is not valid, it forces the console into a permanent freeze state.
Moving on, region locking was done by slightly altering the shape of the cartridge on a region basis, so users could not physically insert the game on a console from a different region.
Overall, piracy wasn’t a significant concern due to the inherent complexity and cost of replicating cartridges, though game prices were often three times higher than CD-based titles.
### Unused ports
As silly as it may seem, Nintendo left one door open: The **Disk Drive port**.
  * [Attached](https://www.copetti.org/writings/consoles/nintendo-64#nestedtab-4-1-attached)
  * [Back](https://www.copetti.org/writings/consoles/nintendo-64#nestedtab-4-2-back)

[![Image](https://www.copetti.org/images/consoles/nintendo64/v64/attached.cbc200b121e31ac928b46fd35c00ef3d1bccb14df0f291fe609b19c21bb0da25.png)](https://www.copetti.org/images/consoles/nintendo64/v64/attached.cbc200b121e31ac928b46fd35c00ef3d1bccb14df0f291fe609b19c21bb0da25.png)The Doctor V64 attached to the console [[46]](https://www.copetti.org/writings/consoles/nintendo-64#bib:photography-amos).[![Image](https://www.copetti.org/images/consoles/nintendo64/v64/back.a72db6ac5ed0ccb548b9980373e32942680c26e0aaa36db6273af0046b0a1e24.png)](https://www.copetti.org/images/consoles/nintendo64/v64/back.a72db6ac5ed0ccb548b9980373e32942680c26e0aaa36db6273af0046b0a1e24.png)The back of the V64 [[47]](https://www.copetti.org/writings/consoles/nintendo-64#bib:photography-amos), showing some interesting A/V.
A few companies reversed-engineered the interface to develop their own peripherals, and some of the resulting products became a concern for piracy.
I guess the most notable case was the **Doctor v64** , a device resembling the Disk Drive but equipped with a CD-ROM drive instead.
This expansion could back up the contents of the cartridge to a CD, the opposite (reading ROM files from a CD) was also supported.
### Emulation
When I was a kid, I used to play some N64 games on a Pentium II machine using an emulator. It wasn’t _that bad_ , though in hindsight, I’m amazed my old computer managed to emulate a complex 64-bit machine - especially given that, among other things, my PC barely had enough RAM to keep the integrated video alive.
The truth is, while reproducing the architecture of this console can be complex, microcode routines will give a hint of what the console is trying to achieve, and since emulators _don’t have to be_ cycle-accurate, they can apply enough optimisations to provide extra performance in exchange for precision [[48]](https://www.copetti.org/writings/consoles/nintendo-64#bib:games-frame_emulation).
Another reason is the 64-bit instruction set: since games rarely took full advantage of them, emulation performance was hardly affected when running on a 32-bit host computer.
* * *
## That’s all folks
[![Image](https://www.copetti.org/images/consoles/nintendo64/n64.a1c54350ea9ae2abf8cc131b0f9b191e6bf515eaa47098b6d4ec41e33ee249d2.jpeg)](https://www.copetti.org/images/consoles/nintendo64/n64.a1c54350ea9ae2abf8cc131b0f9b191e6bf515eaa47098b6d4ec41e33ee249d2.jpeg)My _timeshared_ N64 at a friend’s house. While I only wanted the console for the article, my friend had long dreamed of owning a 64DD. So, we bought a complete (and pricey) Japanese set together to split the cost. I then installed the N64RGB mod so we could hook it up to a modern TV. The result is a nice entertainment setup (and a great conversation piece!).
I have to say, this article may be the longest one I’ve ever written, but hopefully you found it a nice read!
I’ll probably take the following days to tide up some things on the website instead of starting to write the next article.
Until next time!  
Rodrigo
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
- Any Dev kit (only if found at a reasonable price)
```

Alternatively, you can help out by [suggesting changes](https://github.com/flipacholas/Architecture-of-consoles) and/or [adding translations](https://github.com/flipacholas/Architecture-of-consoles).
* * *
## Copyright and permissions
This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). You may use it for your work at no cost, even for commercial purposes. But you have to respect the license and reference the article properly. Please take a look at the following guidelines and permissions:
Article information and referencing
For any referencing style, you can use the following information:
  * **Title of article** : Nintendo 64 Architecture - A Practical Analysis
  * **Author** : Rodrigo Copetti
  * **URL** : <https://www.copetti.org/writings/consoles/nintendo-64/>
  * **Date of publication** : September 12, 2019
  * **Last modified** : August 11, 2025


For instance, to use with BibTeX:
```
@misc{copetti-nintendo64,
    url = {https://www.copetti.org/writings/consoles/nintendo-64/},
    title = {Nintendo 64 Architecture - A Practical Analysis},
    author = {Rodrigo Copetti},
    year = {2019}
}

```

or a IEEE style citation:
```
[1]R. Copetti, "Nintendo 64 Architecture - A Practical Analysis", Copetti.org, 2019. [Online]. Available: https://www.copetti.org/writings/consoles/nintendo-64/. [Accessed: day- month- year].

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
  * Mike Ryan, marshallh, John McMaster, [Reversing the nintendo 64 CIC - REcon 2015](https://www.youtube.com/watch?v=HwEdqAb2l50). Youtube. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:45)


### Audio
  * N64brew Wiki contributors, [Memory_map](https://n64brew.dev/wiki/Memory_map) (accessed 05-August-2025). N64brew Wiki. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:16)
  * N64brew Wiki contributors, [Audio interface](https://n64brew.dev/wiki/Audio_Interface) (accessed 05-August-2025). N64brew Wiki. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:28)
  * Dietrich Epp, [Nintendo 64 part 13: Basic audio](https://www.moria.us/blog/2020/11/n64-part13-basic-audio) (accessed 05-August-2025). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:27)


### Audio / Video
  * retroreversing.com, [Pre-written microcodes](https://www.retroreversing.com/n64rsp#pre-written-microcodes). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:20)


### Bonus
  * NEC, [Laserjet printers use the same CPU!](http://www.nec.co.jp/press/en/9801/2002.html).


### CPU
  * Tom R. Halfhill, [Mips challenges intel on its own turf](https://www.halfhill.com/byte/1993-6_mips.html). BYTE. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:1)
  * Tom Plaskon, [Anatomy of a nintendo 64](https://tomplaskon.wordpress.com/2014/06/30/anatomy-of-a-nintendo-64/). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:2)
  * NEC, [VR4300, VR4305, VR4310 user’s manual - 7th edition](http://datasheets.chipdb.org/NEC/Vr-Series/Vr43xx/U10504EJ7V0UMJ1.pdf). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:25)
  * MIPS, [R4300i microprocessor product information - rev 0.3](http://datasheets.chipdb.org/MIPS/R4300i_datasheet.pdf). April 1997.
  * Raymond Chen, [The MIPS R4000, part 8: Control transfer](https://devblogs.microsoft.com/oldnewthing/20180411-00/?p=98485). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:4)
  * Encryption 64, [N64 memory](https://web.archive.org/web/20200430063847/http://en64.shoutwiki.com/wiki/N64_Memory). Archived. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:5)
  * Nintendo Power, [The dream team](https://ia801504.us.archive.org/0/items/Nintendo_Power_Issue001-Issue127/Nintendo%20Power%20Issue%20071%20April%201995.pdf). 1995. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:9)
  * NEC Electronics, Application specific memory 1995 data book. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:11)
  * overclockers.com, [RDRAM/DDR: Part 1, technical aspects](https://www.overclockers.com/rdramddr-part-1-technical-aspects/). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:7)
  * N64brew Wiki contributors, [RDRAM](https://https://n64brew.dev/wiki/RDRAM) (accessed 01-August-2025). N64brew Wiki. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:15)
  * bentomo, [Reverse engineering the jumper pak.](https://forums.modretro.com/threads/reverse-engineering-the-jumper-pak.628/) (accessed 01-August-2025). The Official ModRetro Forums. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:14)
  * overclockers.com, [RDRAM/DDR: Part 1, technical aspects](https://www.overclockers.com/rdramddr-part-1-technical-aspects/). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:7)
  * beyond3d.com, [RDRAM inside the N64](https://forum.beyond3d.com/threads/rdram-inside-the-n64.57660/). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:10)
  * beyond3d.com, [N64 RDP/RSP](https://forum.beyond3d.com/threads/n64-rdp-rsp.15758/). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:8)


### Games
  * GameboyMicro, [A look inside some nintendo 64 games](https://imgur.com/gallery/KteOi). Imgur, 2016.
  * n64squid.com, [Nintendo 64 development hardware](https://n64squid.com/homebrew/n64-sdk/development-hardware/). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:40)
  * n64devkit.square7.ch, [About /dev/u64](http://n64devkit.square7.ch/n64man/u64/u64.htm). 1999. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:41)
  * RetroReversing, [Official nintendo 64 SDK](https://www.retroreversing.com/n64-sdk) (accessed 05-August-2025). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:44)
  * RetroReversing, [N64 RSP - reality signal processor](https://www.retroreversing.com/n64rsp) (accessed 05-August-2025). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:39)
  * gonetz, [Frame buffer emulation. Part i.](https://gliden64.blogspot.com/2013/11/frame-buffer-emulation-part-i.html) (accessed 05-August-2025). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:48)
  * N64brew Wiki contributors, [Peripheral interface](https://n64brew.dev/wiki/Peripheral_Interface) (accessed 05-August-2025). N64brew Wiki. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:37)


### Graphics
  * Jennifer Taylor, [RCP documentation rev.6](https://dragonminded.com/n64dev/Reality%20Coprocessor.pdf). 2010. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:19)
  * N64brew Wiki contributors, [Reality signal processor/CPU core](https://n64brew.dev/wiki/Reality_Signal_Processor/CPU_Core) (accessed 05-August-2025). N64brew Wiki. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:18)
  * N64brew Wiki contributors, [Reality display processor/pipeline](https://n64brew.dev/wiki/Reality_Display_Processor/Pipeline) (accessed 05-August-2025). N64brew Wiki. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:21)
  * Hack64, [RCP structures](https://hack64.net/wiki/doku.php?id=rcpstructs) (accessed 05-August-2025). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:23)
  * N64brew Wiki contributors, [Video DAC](https://n64brew.dev/wiki/Video_DAC) (accessed 05-August-2025). N64brew Wiki. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:26)
  * N64brew Wiki contributors, [Video interface](https://n64brew.dev/wiki/Video_Interface) (accessed 05-August-2025). N64brew Wiki. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:24)


### I/O
  * N64brew Wiki contributors, [Serial interface](https://n64brew.dev/wiki/Serial_Interface) (accessed 05-August-2025). N64brew Wiki. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:36)


### Operating System
  * N64brew Wiki contributors, [Initial program load](https://n64brew.dev/w/index.php?title=Initial_Program_Load) (accessed 11-August-2025). N64brew Wiki. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:32)
  * Decompals, [N64-IPL](https://github.com/decompals/N64-IPL) (accessed 11-August-2025). Github. [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:31)
  * Dietrich Epp, [Nintendo 64 part 11: Scheduling RCP tasks](https://www.moria.us/blog/2020/11/n64-part11-scheduling-rcp-tasks) (accessed 05-August-2025). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:29)


### Photography
  * Evan Amos, [The vanamo online game museum](https://commons.wikimedia.org/wiki/User:Evan-Amos). [↩︎](https://www.copetti.org/writings/consoles/nintendo-64#bibref:47)
  * Rodrigo Copetti (Me), [Diagrams, casual photos, screenshots and videos](https://www.copetti.org/).


* * *
## Changelog
It’s always nice to keep a record of changes. For a complete report, you can check the [commit log](https://github.com/flipacholas/Architecture-of-consoles/commits/master/articles/nintendo-64.Rmd.md). Alternatively, here’s a simplified list:
```
### 2025-08-06
- Overall improvements to prepare for a book release.
### 2025-04-20
- Added photograph of MIPS chip after a quick visit to The Computer History Museum (Mountain View, California) in March 2025.
### 2024-08-06
- Expanded imagery after visiting Cambridge, UK.
### 2022-06-06
- Added section about boot process.
- Renamed the 'Peripheral interface' chip to PIF-NUS (or PIF) according to @Bigbass.
### 2021-07-03
- Added more photography from Evan Amos gallery
### 2021-05-23
- Added more info about 64-bit mode
- Added section about MMU and TLB
- Expanded 64DD section
- Replaced vague terms with more appropriate ones
- Improved 'Sources' structure
### 2020-09-23
- Added info about video out
### 2020-05-20
- Avoid mixing up TMEM with actual Texture cache. Thanks monocasa from Hackernews
### 2020-05-08
- Added Mario 64 screenshot with original resolution
### 2020-04-22
- Improved 9-bit explanation. Thanks /u/mallardtheduck
### 2020-04-14
- Small changes to perspective correction info
### 2020-04-11
- Dedicated more text to the visibility approach 
### 2020-02-26
- Expanded texture unit section.
### 2020-01-11
- Added repertoire
### 2019-10-29
- Added some 3d models to fiddle with
### 2019-09-17
- Added a quick introduction
- Corrected some explanations
### 2019-09-12
- Released to the public, yay
```

* * *
[« Virtual Boy Architecture](https://www.copetti.org/writings/consoles/virtual-boy/) [Dreamcast Architecture »](https://www.copetti.org/writings/consoles/dreamcast/)
![Rodrigo Copetti](https://www.copetti.org/favicon/favicon.png)
### Rodrigo Copetti
I hope you have enjoyed this article! If you want to know more about the author [tap here](https://www.copetti.org/about/) and if you would like to support him [tap here](https://www.copetti.org/support/) instead
[Tweet ](https://twitter.com/intent/tweet?text=Nintendo%2064%20Architecture%20%7c%20A%20Practical%20Analysis%20https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fnintendo-64%2f)[Share ](javascript:void\(0\))[Share ](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fnintendo-64%2f&title=Nintendo%2064%20Architecture%20%7c%20A%20Practical%20Analysis&summary=An%20in-depth%20analysis%20that%20explains%20how%20this%20console%20works%20internally&source=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fnintendo-64%2f)[Share](https://reddit.com/submit?url=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fnintendo-64%2f&title=Nintendo%2064%20Architecture%20%7c%20A%20Practical%20Analysis)
[Switch to classic edition](https://classic.copetti.org/writings/consoles/nintendo-64/)
Rodrigo Copetti © 2025 [](https://www.copetti.org/index.xml)
[About the website and its content](https://www.copetti.org/disclaimer/)
rsslinkedintwitterblueskygithub facebookreddit
