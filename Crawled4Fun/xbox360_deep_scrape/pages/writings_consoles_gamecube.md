# GameCube Architecture | A Practical Analysis

**Source:** https://www.copetti.org/writings/consoles/gamecube

[Home](https://www.copetti.org/)
[Consoles](https://www.copetti.org/writings/consoles/)
[About](https://www.copetti.org/about/)
[Support](https://www.copetti.org/support/)
# GameCube Architecture
## A practical analysis by Rodrigo Copetti
[](https://github.com/flipacholas/Architecture-of-consoles)[](https://crowdin.com/project/architecture-of-consoles)[](https://www.copetti.org/writings/consoles/materials/readings/)[](https://www.copetti.org/writings/consoles/gamecube)
If you use accessibility tools or old browsers, [switch to the ‘classic’ edition](https://classic.copetti.org/writings/consoles/gamecube/).
🇬🇧 - English 🇪🇸 - Español 🇹🇷 - Türkçe 🇨🇳 - 简体字 👋 - Add translation
* * *
Book edition
[![eBook edition](https://www.copetti.org/images/consoles/_covers/en/gamecube_hu_493449fb6d5f0922.jpg)](https://www.copetti.org/writings/consoles/materials/book/)
This article is also published in many bookstores for the benefit of offline readers. The eBooks are DRM-free, while the printed editions compile multiple articles and feature original photography at full resolution.
You can find printed compilations [here](https://www.amazon.com/dp/B0F4P5RB25?binding=paperback), and individual eBooks at [Amazon Kindle](https://www.amazon.com/dp/B0B5VM3NHS), [Apple Books](https://books.apple.com/us/author/rodrigo-copetti/id1632545359?see-all=books), [Kobo](https://www.kobo.com/us/en/search?query=Architecture+of+Consoles%3a+A+Practical+Analysis&fcsearchfield=Series&seriesId=7e46f843-4aee-53b4-97c2-82782e951af5) and [other stores](https://www.copetti.org/writings/consoles/materials/book/). The proceeds support the improvement of current articles and the development of new ones.
For more information, please take a look at [here](https://www.copetti.org/writings/consoles/materials/book/).
* * *
Table of Contents
  1. [Supporting imagery](https://www.copetti.org/writings/consoles/gamecube#imagery)
  2. [A quick introduction](https://www.copetti.org/writings/consoles/gamecube#a-quick-introduction)
  3. [CPU](https://www.copetti.org/writings/consoles/gamecube#cpu)
    1. [The origins of PowerPC](https://www.copetti.org/writings/consoles/gamecube#the-origins-of-powerpc)
      1. [The commercial milestone](https://www.copetti.org/writings/consoles/gamecube#tab-1-1-the-commercial-milestone)
      2. [Reaching the average user](https://www.copetti.org/writings/consoles/gamecube#tab-1-2-reaching-the-average-user)
      3. [Popularising the PowerPC](https://www.copetti.org/writings/consoles/gamecube#tab-1-3-popularising-the-powerpc)
    2. [Contemporary work](https://www.copetti.org/writings/consoles/gamecube#contemporary-work)
      1. [Individual developments](https://www.copetti.org/writings/consoles/gamecube#tab-2-1-individual-developments)
      2. [Joining forces again](https://www.copetti.org/writings/consoles/gamecube#tab-2-2-joining-forces-again)
      3. [The band splits for good](https://www.copetti.org/writings/consoles/gamecube#tab-2-3-the-band-splits-for-good)
    3. [The PowerPC Gekko](https://www.copetti.org/writings/consoles/gamecube#the-powerpc-gekko)
    4. [IBM’s enhancements](https://www.copetti.org/writings/consoles/gamecube#ibms-enhancements)
    5. [A step forward or a step backwards?](https://www.copetti.org/writings/consoles/gamecube#a-step-forward-or-a-step-backwards)
    6. [Clever memory system](https://www.copetti.org/writings/consoles/gamecube#clever-memory-system)
    7. [Making the most of ARAM](https://www.copetti.org/writings/consoles/gamecube#making-the-most-of-aram)
  4. [Graphics](https://www.copetti.org/writings/consoles/gamecube#graphics)
    1. [Architecture and design](https://www.copetti.org/writings/consoles/gamecube#architecture-and-design)
      1. [Database](https://www.copetti.org/writings/consoles/gamecube#tab-3-1-database)
      2. [Geometry](https://www.copetti.org/writings/consoles/gamecube#tab-3-2-geometry)
      3. [Texture](https://www.copetti.org/writings/consoles/gamecube#tab-3-3-texture)
      4. [Render](https://www.copetti.org/writings/consoles/gamecube#tab-3-4-render)
    2. [Interactive comparison](https://www.copetti.org/writings/consoles/gamecube#interactive-comparison)
      1. [The upgrade](https://www.copetti.org/writings/consoles/gamecube#tab-4-1-the-upgrade)
      2. [The update](https://www.copetti.org/writings/consoles/gamecube#tab-4-2-the-update)
    3. [Creativity](https://www.copetti.org/writings/consoles/gamecube#creativity)
    4. [Video output system](https://www.copetti.org/writings/consoles/gamecube#video-output-system)
    5. [Connections](https://www.copetti.org/writings/consoles/gamecube#connections)
  5. [Audio](https://www.copetti.org/writings/consoles/gamecube#audio)
    1. [Compression and freedom](https://www.copetti.org/writings/consoles/gamecube#compression-and-freedom)
      1. [Additional material](https://www.copetti.org/writings/consoles/gamecube#additional-material)
  6. [I/O](https://www.copetti.org/writings/consoles/gamecube#io)
    1. [Internal I/O](https://www.copetti.org/writings/consoles/gamecube#internal-io)
    2. [Optional I/O](https://www.copetti.org/writings/consoles/gamecube#optional-io)
    3. [Unusual I/O](https://www.copetti.org/writings/consoles/gamecube#unusual-io)
    4. [Consistent design](https://www.copetti.org/writings/consoles/gamecube#consistent-design)
  7. [Operating System](https://www.copetti.org/writings/consoles/gamecube#operating-system)
    1. [Splash and shell](https://www.copetti.org/writings/consoles/gamecube#splash-and-shell)
  8. [Games](https://www.copetti.org/writings/consoles/gamecube#games)
    1. [Specialised hardware](https://www.copetti.org/writings/consoles/gamecube#specialised-hardware)
    2. [Medium](https://www.copetti.org/writings/consoles/gamecube#medium)
    3. [Unusual controllers](https://www.copetti.org/writings/consoles/gamecube#unusual-controllers)
    4. [Online Platform](https://www.copetti.org/writings/consoles/gamecube#online-platform)
  9. [Anti-Piracy & Homebrew](https://www.copetti.org/writings/consoles/gamecube#anti-piracy-homebrew)
    1. [Security mechanisms](https://www.copetti.org/writings/consoles/gamecube#security-mechanisms)
      1. [DVD controller](https://www.copetti.org/writings/consoles/gamecube#tab-5-1-dvd-controller)
      2. [IPL and EXI](https://www.copetti.org/writings/consoles/gamecube#tab-5-2-ipl-and-exi)
      3. [Honourable Mention](https://www.copetti.org/writings/consoles/gamecube#tab-5-3-honourable-mention)
  10. [That’s all folks](https://www.copetti.org/writings/consoles/gamecube#thats-all-folks)
  11. [Copyright and permissions](https://www.copetti.org/writings/consoles/gamecube#referencing)
  12. [Sources / Keep Reading](https://www.copetti.org/writings/consoles/gamecube#sources)
  13. [Contributing](https://www.copetti.org/writings/consoles/gamecube#contributing)
  14. [Changelog](https://www.copetti.org/writings/consoles/gamecube#changelog)


* * *
## Supporting imagery
  * [Model](https://www.copetti.org/writings/consoles/gamecube#cover-model)
  * [Motherboard](https://www.copetti.org/writings/consoles/gamecube#cover-motherboard)
  * [Diagram](https://www.copetti.org/writings/consoles/gamecube#cover-diagram)


### Model
[![Model](https://www.copetti.org/images/consoles/gamecube/international.9c16620a2941a4495bc19dee59692e099115038205b5f2ab57942ea3e9df35d6.png)](https://www.copetti.org/images/consoles/gamecube/international.9c16620a2941a4495bc19dee59692e099115038205b5f2ab57942ea3e9df35d6.png)The one and only GameCube.  
Released on 14/09/2001 in Japan, 18/11/2001 in America and 03/05/2002 in Europe.
### Motherboard
  * [Original](https://www.copetti.org/writings/consoles/gamecube#cover-motherboard-original)
  * [Marked](https://www.copetti.org/writings/consoles/gamecube#cover-motherboard-marked)

[![Motherboard](https://www.copetti.org/images/consoles/gamecube/motherboard.241b77ac3c5f924556aa37572c1f9dc4ee9025e1faac05689240bcf7495b4313.png)](https://www.copetti.org/images/consoles/gamecube/motherboard.241b77ac3c5f924556aa37572c1f9dc4ee9025e1faac05689240bcf7495b4313.png)Motherboard  
Taken from my 'DOL-CPU-10' model, later ones removed Serial Port 2 and Digital Output. Encoder chip, expansion, controller and PSU slots are found on the other side.[![Motherboard](https://www.copetti.org/images/consoles/gamecube/motherboard_marked.d838090ff560f6fcac250bb3d7426e0a8d912b9d4e61c0c734cb2f911bdd4f65.png)](https://www.copetti.org/images/consoles/gamecube/motherboard_marked.d838090ff560f6fcac250bb3d7426e0a8d912b9d4e61c0c734cb2f911bdd4f65.png)Motherboard with important parts labelled
### Diagram
[![Diagram](https://www.copetti.org/images/consoles/gamecube/_diagrams/main.b3ccdddb9a7b28e695ebab31ebab7debf79947d8ae681181f690ee5a2768854d.png)](https://www.copetti.org/images/consoles/gamecube/_diagrams/main.b3ccdddb9a7b28e695ebab31ebab7debf79947d8ae681181f690ee5a2768854d.png)Main architecture diagram  
Each data bus is labelled with its width.
* * *
## A quick introduction
Gone are the days of ‘3D-attempts’, Nintendo’s new offering consists of a clean and powerful break from its predecessor that will open the door to new, original and unseen content.
It’s worth pointing out that the design of this architecture led to one of the most compact hardware of this generation. This was emphasised by the lack of _slims_ or _lite_ revisions.
* * *
## CPU
After the loss of [SGI’s dominance](https://www.copetti.org/writings/consoles/nintendo-64/#cpu) in the graphics market, Nintendo needed new players to partner up with.
A promising candidate seems to be **IBM** : Apart from their famous work on mainframes, they recently joined forces with Motorola and Apple to create a CPU powerful enough to compete with Intel’s ruling in the PC market. The resulting product is a series of processors carrying the name **PowerPC** , which were selected to _power_ 99% of Apple’s Macintoshes, IBM’s workstations and some embedded systems.
[![Image](https://www.copetti.org/images/consoles/gamecube/cpu.7bd28c467915a77e6e19d0fccf223504b7d66a8e597bdecc894cf3ca894e217a_hu_980d5447263fd592.png)](https://www.copetti.org/images/consoles/gamecube/cpu.7bd28c467915a77e6e19d0fccf223504b7d66a8e597bdecc894cf3ca894e217a.webp)The PowerPC Gekko chip. This is what the GameCube houses.
To understand what this means for the GameCube, let’s first take a look at the chain of innovation that culminated in the PowerPC CPU.
### The origins of PowerPC
IBM was one of the three early forces pushing for the emerging [RISC CPU design](https://www.copetti.org/writings/consoles/playstation/#tab-1-1-a-bit-of-history) into the mainstream market. During the 80s, while Berkeley was busy developing the ‘RISC CPU’ and Stanford academics [just founded MIPS](https://www.copetti.org/writings/consoles/playstation/#tab-1-2-mips-and-sony), IBM had already produced the **801** and **ROMP** CPUs. These were ground-breaking yet commercially-unsuccessful silicon implementing a set of guidelines later known as the ‘RISC model’ [[1]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-diefendorff_601).
  * [The commercial milestone](https://www.copetti.org/writings/consoles/gamecube#tab-1-1-the-commercial-milestone)
  * [Reaching the average user](https://www.copetti.org/writings/consoles/gamecube#tab-1-2-reaching-the-average-user)
  * [Popularising the PowerPC](https://www.copetti.org/writings/consoles/gamecube#tab-1-3-popularising-the-powerpc)


#### The commercial milestone
Entering the 90s, IBM tried again with a new series of UNIX workstations called ‘IBM RS/6000’, and within it, a new in-house RISC CPU: **POWER1**. With a focus on [instruction-level parallelism](https://www.copetti.org/writings/consoles/xbox-360/#revisiting-old-paradigms), the latter featured attractive advancements such as [[2]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-power1):
  * A complete 32-bit instruction set called **POWER**.
  * A **64-bit floating-point unit**.
  * A **Harvard cache** architecture, this segregates data and instruction space to increase bandwidth.
  * The ability to execute two instructions at the same time by distributing them across its three separate units (branch, fixed-point and floating-point). Hence, POWER1 is recognised as being **two-way superscalar**.
  * **Static branch prediction** , which turns [control hazards](https://www.copetti.org/writings/consoles/playstation/#delay-galore) into opportunities for accelerating execution.
  * **Out-of-order execution** of floating-point operations, through [register renaming](https://www.copetti.org/writings/consoles/xbox-360/#revisiting-old-paradigms) [[3]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-rs6000). All in all, this greatly increments the amount of instructions the CPU executes per time (and takes care of [data hazards](https://www.copetti.org/writings/consoles/playstation/#delay-galore)).
    * The core design originates from IBM’s mainframe era, when it was published as **Tomasulo’s algorithm** and subsequently implemented on the IBM System/360 (1966). With POWER1, IBM managed to bring part of it to workstation equipment.


Nevertheless, the POWER1 CPU was a large and expensive package comprised of multiple chips. So, for their follow-up venture, IBM shrank down its design to fit in a single chip. While still POWER-compliant, this came at the cost of housing a 32-bit FPU, a von Neumann cache architecture and reverting to in-order execution. The new chip was called **RISC Single Chip** (or ‘RSC’) and shipped with the low-end line of their RS/6000 workstations.
« Previous [Next »](https://www.copetti.org/writings/consoles/gamecube#tab-1-2-reaching-the-average-user)
#### Reaching the average user
[![Image](https://www.copetti.org/images/consoles/gamecube/prototype.c88650e3e2cfe8189bb430f0e0113c22566bdc3dd0ba0a1f3915bfe673f1173f_hu_648c79c8920786a4.png)](https://www.copetti.org/images/consoles/gamecube/prototype.c88650e3e2cfe8189bb430f0e0113c22566bdc3dd0ba0a1f3915bfe673f1173f.webp)IBM’s POWER development board (1992), used by Apple.
In the midsts of these developments, IBM also agreed to join forces with Apple and Motorola to tackle the Intel-Microsoft monopoly in the desktop market, forming the **AIM alliance**. Thus, a new project was conceived for a competitive CPU in the low-end arena. This would be made of intellectual property from the three companies, including:
  * IBM’s RSC processor design.
  * Motorola’s bus architecture (found in their in-house RISC processor, the Motorola 88110).
  * Apple and Motorola’s knowledge of the end-user’s needs.


Keith Diefendorff, a member of the Motorola 88110 team, was recruited as the lead architect and, in 1993, the project culminated in the following:
  * The **PowerPC instruction set** : A subset of POWER, with additional instructions for multiplication, support for a symmetric multiprocessor setup and an optional 64-bit mode.
    * From then on, IBM’s POWER CPU line would implement the PowerPC ISA instead. This was first apparent with the release of POWER3 in 1998, a high-performance CPU implementing the 64-bit specification of PowerPC.
    * We won’t see a symmetric multiprocessor setup in this article series until the [Xbox 360](https://www.copetti.org/writings/consoles/xbox-360/) and [Wii U](https://www.copetti.org/writings/consoles/wiiu/) arrive.
  * The **PowerPC CPU** , a new line of desktop CPUs implementing the PowerPC ISA, starting with the **PowerPC 601**. This was a cost-effective version of the RSC microarchitecture.
    * Motorola also dropped the development of the 88000 CPU altogether to focus on this new series.


[« Previous](https://www.copetti.org/writings/consoles/gamecube#tab-1-1-the-commercial-milestone) [Next »](https://www.copetti.org/writings/consoles/gamecube#tab-1-3-popularising-the-powerpc)
#### Popularising the PowerPC
To make sure the new line would be both technically competitive and commercially viable, the PowerPC 601 attempted to bring certain advancements of instruction parallelism to the masses, to name a few [[4]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-diefendorff_601):
  * The implementation of **both POWER and PowerPC ISAs** , to assist POWER developers in transitioning to PowerPC.
  * **Three-way superscalar execution** using three separate execution units (FPU, branch and ALU) [[5]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-601_report). An improvement from previous designs.
  * Based on Motorola’s model, a new bus design called **Bus Interface Unit** , providing:
    * A **64-bit data bus** and a **32-bit address bus** , the former is critical for taking advantage of the superscalar capabilities.
    * **Burst transactions** , enabling to transfer 32 Bytes of memory (the size of L1 cache) with a single instruction [[6]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-601).
  * **Memory Management Unit** (MMU), offering [virtual memory](https://www.copetti.org/writings/consoles/nintendo-64/#memory-management) in the same package.


For the end user, this new CPU would now be found in IBM’s low-end RS/6000 series and in Apple’s new line of Macintosh computers called ‘Power Macintosh’.
[« Previous](https://www.copetti.org/writings/consoles/gamecube#tab-1-2-reaching-the-average-user) Next »
### Contemporary work
The PowerPC 601 was meant to kickstart momentum for the PowerPC line, but the following years saw turbulent changes in the microarchitecture.
  * [Individual developments](https://www.copetti.org/writings/consoles/gamecube#tab-2-1-individual-developments)
  * [Joining forces again](https://www.copetti.org/writings/consoles/gamecube#tab-2-2-joining-forces-again)
  * [The band splits for good](https://www.copetti.org/writings/consoles/gamecube#tab-2-3-the-band-splits-for-good)


#### Individual developments
Once the 601 shipped, Motorola and IBM decided to separately work on the follow-up generation. This would be a pure PowerPC implementation (removing traces of the POWER ISA) materialising as two separate product lines [[7]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-paradox):
  * The low-end **PowerPC 603** , headed by Motorola, was designed for the portable market. In doing so, it delivered a smaller L1 cache (now based on the Harvard architecture), two additional execution units and no multiprocessor support. The design decisions resulted in an overall consumption rate of 1.8-2.0 Watts [[8]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-603).
  * The high-end **PowerPC 604** headed by IBM. In exchange for a premium price and high power consumption (14.5-18.5 Watts), it provided advanced parallelism capabilities ([à la MIPS](https://www.copetti.org/writings/consoles/playstation-2/#tab-1-1-outperforming-success)), such as 4-issue execution, the return of out-of-order execution, dynamic branch prediction and multiprocessor support [[9]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-604).


Even though the 603 should’ve shined for its power efficiently, existing business applications ended up eclipsing its novelties. For instance, Apple’s software architecture was still relying on emulating [68000 instructions](https://www.copetti.org/writings/consoles/mega-drive-genesis/#the-leader), which bottlenecked the 603’s small cache size.
As a side note, IBM also developed the **PowerPC 4xx** series, conceived as a microcontroller solution instead of a desktop CPU [[10]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-403). They bundle small cache and skip sophisticated modules such as the MMU and FPU. However, their variants were offered as a [customisable package](https://www.copetti.org/writings/consoles/playstation/#tab-1-3-lsi-and-the-commission) to tailor it to the manufacturer’s needs. That being said, while the 4xx is not of particular interest for this article, a famous competitor [did adopt it](https://www.copetti.org/writings/consoles/playstation-2/#the-special-upgrade) for secondary tasks.
« Previous [Next »](https://www.copetti.org/writings/consoles/gamecube#tab-2-2-joining-forces-again)
#### Joining forces again
Ultimately, the second generation of desktop PowerPC chips was deemed either too expensive or downright uncompetitive against Intel. Thus, Apple got IBM and Motorola to collaborate again in a new unified generation that brought out the best of both worlds. The energy-efficient 603 was chosen as the foundation for the new design. To improve upon this basis, certain decisions were taken:
  * **Addressing its limitations** by providing larger cache and higher memory bandwidth.
  * **Incorporating design ideas of the 604** , such as dynamic branch prediction and out-of-order execution (limited to memory operations, for now).
  * **Implementing new enhancements** , such as an extra ALU for greater parallelism.


This became the **750 line** , popularised by Apple as the **PowerPC G3**. From then on, IBM and Motorola continued working on variants and enhancements of the 750. These focused on greater clock speeds, larger cache and smaller fabrication process.
Interestingly, it’s always the most energy-efficient CPUs that manage to weather development turmoil, as others ([MIPS](https://www.copetti.org/writings/consoles/playstation-portable/#mips-after-the-turn-of-the-century), [Intel](https://www.copetti.org/writings/consoles/xbox/#p6-and-the-end-of-pentium-numbers) and [ARM](https://www.copetti.org/writings/consoles/nintendo-ds/#arms-new-territories)) will later corroborate.
[« Previous](https://www.copetti.org/writings/consoles/gamecube#tab-2-1-individual-developments) [Next »](https://www.copetti.org/writings/consoles/gamecube#tab-2-3-the-band-splits-for-good)
#### The band splits for good
As time passed, the three companies became increasingly distant. Two years after the PowerPC G3 was unveiled, Motorola delivered by itself a new line called the **7400** (which Apple named the **G4**). This featured a 64-bit FPU, a faster bus architecture called ‘MPX’ and a set of SIMD instructions called ‘Altivec’. Despite its popularity in the desktop market (thanks to Apple), IBM only devoted attention to its exclusive POWER CPU line.
Years later, in 2003, Motorola finally gave up on the CPU business and divested its semiconductor division, leading to the incorporation of ‘Freescale’. The latter wasn’t interested in working on PowerPC chips either, and so the **AIM alliance came to an end**. Be as it may, Apple still needed new CPUs, so IBM continued the line of succession by grabbing its POWER4 design and scaling it down, leading to the PowerPC 970 CPU (also called the ‘G5’).
And this is where the history section ends. Thus, it’s time to take a look at the GameCube’s unique CPU (which sits between the 750/G3 and the 7400/G4). Now, I’ll be focusing on the GameCube hardware from now on, but if this detour got your attention, you may want to read the [PlayStation 3](https://www.copetti.org/writings/consoles/playstation-3/), [Xbox 360](https://www.copetti.org/writings/consoles/xbox-360/) and [Wii U](https://www.copetti.org/writings/consoles/wiiu/) studies next.
[« Previous](https://www.copetti.org/writings/consoles/gamecube#tab-2-2-joining-forces-again) Next »
### The PowerPC Gekko
Back to the year 2001, Nintendo required something powerful but cheap. So, to comply with those red lines, IBM grabbed one of its past designs, an enhanced G3 called the **PowerPC 750CXe** (found on the late iMac G3, known as the _Early-Summer 2001_), and beefed it up with capabilities that would please game developers. The result was the **PowerPC Gekko** and runs at **486 MHz**.
[![Image](https://www.copetti.org/images/consoles/gamecube/_diagrams/gekko.8c2eb3b88fcc568953ea3e13084729c2b59bdb3794b024b6d85bb3697e85ff53.png)](https://www.copetti.org/images/consoles/gamecube/_diagrams/gekko.8c2eb3b88fcc568953ea3e13084729c2b59bdb3794b024b6d85bb3697e85ff53.png)Construction of Gekko.
Let’s find out what makes Gekko so special, and to do that we need to first look at the offerings of the 750CXe. Now, having gone through the history of PowerPC, you may find that a lot this information overlaps with previous designs (_that’s the point of these studies!_). That being said, the 750CXe offers [[11]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-750cxe):
  * The **PowerPC ISA** : This comes as no surprise. The only additional information is that the 750CXe implements the v1.10 specification.
  * External **64-bit data bus** : As you’ve seen before, while the ISA can fit in a 32-bit bus, we still need to move wider chunks of data without hitting performance penalties.
  * **Triple-issue superscalar** : If the required units are available, the CPU may process up to two instructions at the same stage of the pipeline. In the case the queue includes a branching instruction, the number of possible concurrent instructions is raised to three.
  * **Out-of-order execution** : The CPU can re-order the sequence of instructions to keep all of its units working, thus increasing efficiency and performance.
  * **Two Integer Units** : Combined with the superscalar and out-of-order model, it increments the number of integer operations done per unit of time.
  * **Integrated FPU** with 32-bit and 64-bit registers: Accelerates operations with floats and doubles.
  * **Four-stage pipeline (with bonus)** : [Here](https://www.copetti.org/writings/consoles/game-boy-advance/#cpu) is a previous introduction to instruction pipelining. In the 750CXe, FPU operations are divided into three more stages (7 stages in total) while load-store operations are divided into two (5 stages in total).
    * All in all, this increments the instruction throughput without [getting out of hand](https://www.copetti.org/writings/consoles/xbox/#tab-1-3-the-microarchitecture).


Additionally, this CPU also includes dedicated units to speed up specific computations [[12]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-stokes):
  * **Branch Prediction Unit** : Whenever there is a condition that needs to be evaluated (which would decide if the CPU should follow path ‘A’ or path ‘B’), the CPU will instead follow one of the paths based on previous executions and then evaluate the condition. If the prediction happens to be right then the CPU will have saved some time, if not, it will reverse and follow the correct path.
  * **Dedicated load-store unit** : Separates the units that manipulate registers and the ones handling main memory.
  * **Integrated Memory Management Unit** : Interfaces all memory access from the CPU.
    * Previous consoles included this component as another co-processor, the MMU is now found inside the same chip, reducing manufacturing costs.


And, of course, some cache is also included to speed up memory bandwidth:
  * **64 KB L1 cache** : Divided into 32 KB for instructions and 32 KB for data.
  * **256 KB L2 cache** : It can be filled with instructions and data, which greatly improves bandwidth.


### IBM’s enhancements
While the previous lists of features are very appreciated (compared to previous generations), this CPU still falls behind others on gaming performance (let’s not forget that this is still a general-purpose CPU, good at spreadsheets but _average_ at physics). To compensate, IBM added the following tweaks that will constitute Gekko [[13]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-ibm):
  * Enhanced instruction set with **50 new SIMD instructions** : These operate two 32-bit floating-point numbers or one 64-bit floating-point number using only one cycle. Consequently, the new SIMD instructions will speed up vector calculations, particularly useful during geometry transformations.
    * Not to be confused with Motorola’s SIMD extension (AltiVec) which shipped on the PowerPC 7400/G4. They are not compatible with each other. Curiously enough, IBM did eventually implement Altivec in its POWER4 CPU and, by extension, into the 970/G5 series, [Cell](https://www.copetti.org/writings/consoles/playstation-3/#cpu) and [Xenon](https://www.copetti.org/writings/consoles/xbox-360/#cpu).
  * **32 floating-point registers** : These come with the new SIMD instructions.
  * **Write Gather pipe** : A special memory writing mechanism available to use. If enabled, instead of performing _single-beat_ transfers, it holds all memory write requests in a 128-byte buffer until it’s 25% full, then performs the requested writes using a technique called _burst transaction_ which can move blocks of 32 bytes of data at once.
    * As you can imagine, this saves a lot of bandwidth by making full utilisation of the available buses.
  * **Locked L1 cache** : Programs can take away 16 KB of L1 data cache to use as ‘scratchpad’ (incredibly fast memory).


Apart from handling the game logic (physics, collisions, etc), these enhancements will allow the CPU to implement parts of the graphics pipeline (geometry transformations, lighting, etc) with acceptable performance. This is very important since the GPU can only accelerate a limited set of operations, so the end result is not conditioned by the GPU’s limitations.
### A step forward or a step backwards?
> On your [Nintendo 64 article](https://www.copetti.org/writings/consoles/nintendo-64/), you explained that the system has a 64-bit CPU, but the GameCube one is 32-bit. Did Nintendo downgrade their console?
Indeed Gekko implements a 32-bit PowerPC specification, while the MIPS R4300i can switch between 32-bit and 64-bit modes. To answer whether this is an improvement or not, you have to ask yourself: Why would you need ‘64-bitness’?
  * To address more than 4 GB of memory → The GameCube doesn’t have near that amount of memory locations, so this is not a requirement.
  * To operate larger chunks of data using fewer cycles and bandwidth → That’s covered by Gekko’s new SIMD instructions, the 64-bit FPU and data bus; and the write-gather pipe.
  * To come up with more advertising terms → Yeah… I don’t think that persuades people anymore.


As you can see, the GameCube already enjoys the advantages of 64-bit systems without being called a ‘64-bit console’. This is why you and I can’t summarise two complex machines by their ‘number of bits’.
### Clever memory system
During the design of the next-gen architecture, Nintendo’s architects performed a post-mortem analysis of [their previous design](https://www.copetti.org/writings/consoles/nintendo-64/) and discovered that using a Unified Memory architecture together with some high-latency components (RDRAM) resulted in one of the biggest causes of bottlenecks (almost 50% of CPU cycles were wasted while idling) [[14]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-gdc). Moreover, the inclusion of multiple independent units contributed to a concerning competition for the memory bus.
For that reason the GameCube’s architects came up with a new memory system strictly based on **providing dedicated memory space** and **using low-latency chips**. With the new design, GPU and CPU will no longer compete for the same RAM (causing fill-rate issues) since the GPU will now have its own internal and _amazingly_ fast memory. On the other side, the GPU will still be in charge of arbitrating access to I/O too.
[![Image](https://www.copetti.org/images/consoles/gamecube/_diagrams/memory.4690597b9c7542531c3fcba6030c105e1ae5798617d7c4451f15fb3d4fc0be22.png)](https://www.copetti.org/images/consoles/gamecube/_diagrams/memory.4690597b9c7542531c3fcba6030c105e1ae5798617d7c4451f15fb3d4fc0be22.png)Memory layout of this system.
The result was a system organised with two main buses:
  * The **Northbridge** : It’s 64-bit wide and connects the CPU with the GPU. It runs 3 times slower than the CPU clock, so tasks will have to be optimised to not rely so much on the GPU. Other components like the DMA and cache may come in handy.
  * The **Southbridge** : It’s also 64-bit wide and connects the GPU with **24 MB of 1T-SRAM** called ‘Splash’. This type of RAM is made of DRAM (which is the most popular type but also cheaper and slower) however it’s enhanced with extra circuitry to **behave like SRAM** (faster and expensive, mostly used for cache). The bus is **twice as fast as the GPU** , possibly to enable the GPU to provide a steady bandwidth between the CPU and main memory.


Additionally, this design contains an additional (yet unusual) bus where more memory can be found:
  * The **Eastbridge** : It connects the GPU with another memory chip called **Audio RAM** or ‘ARAM’ [[15]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-hitmen). It provides **16 MB of SRAM** available for general purposes, which is pretty big for _spare_ memory. However, the bus is not accessible through normal means (memory addresses). Instead, it’s connected to an 8-bit serial endpoint (clocked two times slower than the GPU and four times slower than the CPU), which is only accessible through DMA.


Overall, this means that while ARAM provides a considerable amount of RAM, it will be limited to less critical tasks, like acting as an audio buffer or being used by certain accessories (explained in the I/O section).
### Making the most of ARAM
So far, we’ve seen that, on paper, the memory capabilities are undoubtedly superior to its predecessor, but there’s still room for improvement. For instance, Nintendo could’ve fitted more hardware to incorporate ARAM into the CPU’s memory map.
On a related note, let’s revisit the MMU used in Gekko. The CPU, with its 32-bit address bus, can access up to 4 GB of memory, but the system houses nowhere near that quantity. So, to prevent exposing unpopulated (and unpredictable) memory addresses, ‘virtual memory’ addressing is activated by default to mask physical addresses with a safer, easily-cacheable and continuous ‘virtual’ address map [[16]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-dolphin_final).
To make this work, Gekko (and other PowerPC architectures) translate virtual addresses to physical ones with the following process:
  1. Perform **Block Address Translation** (BAT): There are eight pairs of programmable registers (four for data and four for instructions) where each pair map a range of virtual address to a continuous range of physical addresses. The MMU attempts to find the physical address if it’s found within those ranges.
  2. If BAT didn’t work, read the **Page Table** : The MMU also stores a table that catalogues the physical location of pages (block of virtual addresses).
     * The MMU can take time to read a page table, so a **Translation look-aside buffer** (TLB) is included to cache recent reads.
     * Other architectures such as x86 or MIPS provide paging as well, though not all of them will offer a TLB.
  3. Finally, if the requested virtual address can’t still be translated, then the MMU triggers a ‘page fault’ exception in the CPU and lets the operating system decide what to do next.


So what use does this have for developers? Well, it turns out Nintendo released some libraries that **extend main RAM using ARAM** with the help of paging. To recap, ARAM is not addressable, but the CPU may call DMA to fetch and store data from there. Thus, the CPU can move pages out of main RAM to make room for other resources and temporarily store them in ARAM. Afterwards, whenever a page fault occurs, the OS contains routines to look for the missing pages in ARAM and restore them to their original location in main RAM.
In conclusion, with some clever tricks, these general-purpose capabilities enabled GameCube games to enjoy more memory than technically allowed, thereby reaching higher levels of quality. However, it’s important to bear in mind that such tricks may come with some performance penalties (especially if they’re taken for granted).
* * *
## Graphics
This is one of the most critical sections of this console, it basically makes the GameCube, a _GameCube_.
The history of this console’s GPU has some interesting connections: Wei Yen, the director of N64’s SoC ([the RCP](https://www.copetti.org/writings/consoles/nintendo-64/#graphics)), later founded ArtX and landed a contract with Nintendo to develop their next-gen chip: **Flipper**.
[![Image](https://www.copetti.org/images/consoles/gamecube/sunshine.1cedc3e40400190bfd4c914b279f5f561a4de58db6f54225d7b7221c7f6787dc.png)](https://www.copetti.org/images/consoles/gamecube/sunshine.1cedc3e40400190bfd4c914b279f5f561a4de58db6f54225d7b7221c7f6787dc.png)Super Mario Sunshine (2002).
There were lots of advancements done from the previous iteration, for instance, the subsystem was severely simplified down to a single (but powerful) core.
During the development process, ArtX got acquired by ATI, which in turn was sold to AMD six years later. Hence, this is why you see an ATI sticker stamped on the front of the case.
### Architecture and design
Flipper is a complex block that handles multiple services [[17]](https://www.copetti.org/writings/consoles/gamecube#bib:graphics-cheng), so let’s focus on the graphics component for now (since it’s the one responsible for bringing our geometry to life). We’ll call this area the **GPU** or **Graphics Engine** and, if you’ve been reading the [N64 article](https://www.copetti.org/writings/consoles/nintendo-64/#graphics), just letting you know that the core is now functional out of the box, so programmers won’t need to worry about injecting code to make it work. Nevertheless, there will be some interesting parts that are customisable.
[![Image](https://www.copetti.org/images/consoles/gamecube/_diagrams/gpu/pipeline.05797922b47f791560013833c33259966805f7f98cb42bde0cd1c6ef1055b4c3.png)](https://www.copetti.org/images/consoles/gamecube/_diagrams/gpu/pipeline.05797922b47f791560013833c33259966805f7f98cb42bde0cd1c6ef1055b4c3.png)Pipeline design of Flipper’s GPU.
As always, in order to draw a frame on the screen, our data will be pumped through the GPU’s pipeline. Data goes through lots of different components which we can group into four stages:
  * [Database](https://www.copetti.org/writings/consoles/gamecube#tab-3-1-database)
  * [Geometry](https://www.copetti.org/writings/consoles/gamecube#tab-3-2-geometry)
  * [Texture](https://www.copetti.org/writings/consoles/gamecube#tab-3-3-texture)
  * [Render](https://www.copetti.org/writings/consoles/gamecube#tab-3-4-render)


#### Database
[![Image](https://www.copetti.org/images/consoles/gamecube/_diagrams/gpu/database.5b3f72b1ab4109cc96398cf978f4af2a0444aae63300e41655f8e980905f25f0.png)](https://www.copetti.org/images/consoles/gamecube/_diagrams/gpu/database.5b3f72b1ab4109cc96398cf978f4af2a0444aae63300e41655f8e980905f25f0.png)Database stage diagrams.
The CPU and GPU communicate to each other using a fixed-length **FIFO buffer** in main RAM, this is a reserved portion where the CPU will write drawing commands that the GPU will read (and eventually display), this functionality is natively supported by the CPU and GPU.
Furthermore, the CPU and GPU don’t have to be pointing at the same FIFO at the same time, so the CPU can fill a separate one while the GPU is reading the first one [[18]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-gdc). This prevents idling.
Issuing individual commands to construct our geometry can get very tedious with complex scenes, so official libraries included tools that generated the required Display Lists (pre-compiled set FIFO commands) from the game’s assets, this chunk only needs to be copied to RAM to let the GPU effectively display them.
The GPU contains a **command processor** which is in charge of fetching commands from FIFO.
« Previous [Next »](https://www.copetti.org/writings/consoles/gamecube#tab-3-2-geometry)
#### Geometry
[![Image](https://www.copetti.org/images/consoles/gamecube/_diagrams/gpu/vertex.ea413adcb66fe70962a865a9eb4bb407259f45660899deca6cb837814feb2941.png)](https://www.copetti.org/images/consoles/gamecube/_diagrams/gpu/vertex.ea413adcb66fe70962a865a9eb4bb407259f45660899deca6cb837814feb2941.png)Vertex stage diagram using indirect mode.
Here primitives are transformed to shape accordingly for the desired scenery and prepared for rasterising. The engine uses a dedicated **Vertex unit** or ‘VU’ to accomplish this.
There are two **vertex modes** available to handle primitives issued through FIFO:
  * **Direct mode** : The CPU issues each FIFO entry with all required attributes (position, normal, colour, texture coordinate, or matrix index). Useful when the data is already cached.
  * **Indirect mode** : The FIFO entry contains an index value that specifies where the attribute information is located in RAM, so the vertex unit needs to look it up by itself. This data is structured as an array, so for the VU to traverse it, each vertex entry must specify where the array starts (**base pointer**), how long is each entry (**stride**) and at which position the vertex is (**index**).


Once loaded, the primitives can be **transformed** , **clipped** , **lighted** (each vertex will have an RGB value that can also be interpolated for Gouraud Shading purposes) and finally, **projected**.
[« Previous](https://www.copetti.org/writings/consoles/gamecube#tab-3-1-database) [Next »](https://www.copetti.org/writings/consoles/gamecube#tab-3-3-texture)
#### Texture
[![Image](https://www.copetti.org/images/consoles/gamecube/_diagrams/gpu/texture.d12341fb8eaaf414c985cb627d0ceb65911819730629433dc056b089756a240b.png)](https://www.copetti.org/images/consoles/gamecube/_diagrams/gpu/texture.d12341fb8eaaf414c985cb627d0ceb65911819730629433dc056b089756a240b.png)Texture stage diagram using a default setup.
Now it’s time to apply textures and effects to our models, and for that the GPU includes multiple units which will process our pixels. Now, this is a very sophisticated (yet quite complex) procedure, so if you find it difficult to follow, just think of it as a big assembly line that processes pixels. Having said that, there are three groups of units available:
  * **Four parallel Pixel units** (also called ‘pixel pipelines’): Rasterises our primitives (converts them to pixels). Having four units available enables to deliver up to 2x2 pixels on each cycle.
  * **One Texture mapping unit** at the end of each Pixel unit (giving **four in total**): Together they process up to eight textures for our primitives (now mere pixels) at each cycle.
    * It can also loop itself to merge multiple texture layers over the same primitive, this feature is called **Multi-Texturing** and can be used to achieve **detailed textures** , **environment mapping** (reflections) and **bump mapping** [[19]](https://www.copetti.org/writings/consoles/gamecube#bib:graphics-staff), for instance.
    * Finally, the unit also provides an **early[z-buffer](https://www.copetti.org/writings/consoles/nintendo-64/#modern-visible-surface-determination)**, **mipmapping** (processing a downsized texture instead, based on the level of detail) and **anisotropic filtering** (a welcoming improvement over the [previous filters](https://www.copetti.org/writings/consoles/nintendo-64/#tab-1-2-reality-display-processor) that provides greater detail with sloped textures).
  * **Texture Environment unit** or ‘TEV’: A very powerful and programmable 16-stage colour blender. It basically combines multiple [texels](https://www.copetti.org/writings/consoles/playstation/#tab-3-5-textures) (lighting, textures and constants) to achieve an immense amount of texture effects that will be applied over our polygons.
    * The unit works by receiving four texels which are then processed based on the operation requested. Afterwards, it can feed itself the resulting texels as new input, so at the next stage/cycle, the unit can perform a different type of operation over the previous result. This ‘loop’ can last up to 15 iterations.
    * Each stage has 2^4 operations to choose from [[20]](https://www.copetti.org/writings/consoles/gamecube#bib:graphics-dolphin_uber) and, considering the result can be re-processed at the next stage, there are ~5.64 × 10^511 possible permutations!
    * Programmers set up the TEV at runtime (meaning it can change any time) and this is crucial since it opens the door to lots of original materials and effects.


All of this is assisted by 1 MB of Texture memory (1T-SRAM type) which can be split into cache and Scratchpad memory (fast RAM). **Real-time hardware decompression** for SRTC (S3 Texture Compression) textures is also available to fit more textures in that single meg. of memory available.
[« Previous](https://www.copetti.org/writings/consoles/gamecube#tab-3-2-geometry) [Next »](https://www.copetti.org/writings/consoles/gamecube#tab-3-4-render)
#### Render
[![Image](https://www.copetti.org/images/consoles/gamecube/_diagrams/gpu/render.bfaf6ba473ca3b0853a087959b830d3d75054cb106e0921d21e8a2f1fad094ef.png)](https://www.copetti.org/images/consoles/gamecube/_diagrams/gpu/render.bfaf6ba473ca3b0853a087959b830d3d75054cb106e0921d21e8a2f1fad094ef.png)Render stage diagram.
The final stage of the rendering process includes applying some optional but useful touches to our scene:
  * **Fog** : Blends the last colour from the TEV with a fog constant colour to effectively simulate a foggy environment.
  * **Z-compare** : A late-stage [Z-buffer](https://www.copetti.org/writings/consoles/nintendo-64/#modern-visible-surface-determination). The engine will use 2 MB of embedded 1T-SRAM for Z-buffering calculations.
  * **Blending** : Combines the colours of the current frame with the previous frame buffer.
  * **Dithering** : As the name indicates, applies dithering over our frame.


The resulting frame is finally written to the frame buffer in the embedded 1T-SRAM, but this is still locked inside Flipper (the area is called ‘Embedded Frame Buffer’ or ‘EFB’, though it also includes the z-buffer). So, to display it on our TV, we have to copy it to the **External Frame-Buffer** or ‘XFB’ [[21]](https://www.copetti.org/writings/consoles/gamecube#bib:graphics-xfb), which can be picked up the **Video Interface** or ‘VI’. Besides, the copy process can apply effects like **Antialiasing** (reduces blocky edges), **Deflicker** (smooths sudden changes in brightness), **RGB to YUV conversion** (a similar format that occupies less space in memory) and **Y-scaling** (vertically scales the frame).
It’s worth mentioning that the XFB area can also be manipulated by the CPU, this enables it to combine previously-rendered bitmaps with our recently-rendered frame; or when certain games need to render very colour-rich frames which can’t fit in the EFB, so they are rendered in parts and merged by the CPU afterwards (always keeping in-sync with the VI).
[« Previous](https://www.copetti.org/writings/consoles/gamecube#tab-3-3-texture) Next »
### Interactive comparison
Time to put all of this into perspective, check out how programmers evolved the designs of their previous games to take advantage of the new graphics capabilities of this console. Don’t forget the examples are interactive!
  * [The upgrade](https://www.copetti.org/writings/consoles/gamecube#tab-4-1-the-upgrade)
  * [The update](https://www.copetti.org/writings/consoles/gamecube#tab-4-2-the-update)


#### The upgrade
The famous Mario model which had to be stripped down due to polygon counting on the [previous generation](https://www.copetti.org/writings/consoles/nintendo-64/) got completely redesigned for this one, take a closer look at how the model evolved from plain faces to wrinkled sleeves.
Wireframe | Surface | Textured  
---|---|---  
![3D model](https://www.copetti.org/images/consoles/models/mario_smash_64.67e4d4841761b02c2d70c952967712466feb269f8ff87a1aeadad304985254fb.png)  
Tap to enable interaction  
Super Smash Bros (1999) for the N64.  
320 triangles. Wireframe | Surface | Textured  
---|---|---  
![3D model](https://www.copetti.org/images/consoles/models/mario_melee_gc.10424603b8041316d32a89841e29c3c74f85cfc76226923181071fbe125217f5.png)  
Tap to enable interaction  
Super Smash Bros. Melee (2001) for the GC.  
4,718 triangles.
It’s really impressive how much detail has been gained in just two years, eh?
« Previous [Next »](https://www.copetti.org/writings/consoles/gamecube#tab-4-2-the-update)
#### The update
In this case, Sonic Team already designed a Sonic model for [their unique console](https://www.copetti.org/writings/consoles/dreamcast/), but after porting their game to the GameCube they found themselves able to add more polygons to their model, achieving better detail.
Wireframe | Surface | Textured  
---|---|---  
![3D model](https://www.copetti.org/images/consoles/models/sonic_adventure_dc.5fc8797f7a8e3890d5ce2d23aa8b4e5f703ab212a4740bd39471ca602d8c7a4b.png)  
Tap to enable interaction  
Sonic Adventure (1999) for the DC.  
1,001 triangles. Wireframe | Surface | Textured  
---|---|---  
![3D model](https://www.copetti.org/images/consoles/models/sonic_dx_gc.41a4e15c6f7f26a75fe7bbec90b37e04a4c553fd33a469ff42593eb60bb5f248.png)  
Tap to enable interaction  
Sonic DX (2003) for the GC.  
1,993 triangles.
[« Previous](https://www.copetti.org/writings/consoles/gamecube#tab-4-1-the-upgrade) Next »
### Creativity
As you can see from the inner working of this pipeline, graphics technology has been evolving to point that programmers can now take control of certain functions of the rendering process.
[![Image](https://www.copetti.org/images/consoles/gamecube/wind_waker.a64dd8728e2be17d9b947694e3c8684b580bb901e565398a65691ec7d4218a53.png)](https://www.copetti.org/images/consoles/gamecube/wind_waker.a64dd8728e2be17d9b947694e3c8684b580bb901e565398a65691ec7d4218a53.png)The Legend of Zelda: The Wind Waker (2003).
During the same time, PC graphics cards were starting to discard fixed-function pipelines in favour of **shader cores** (units that run small programs which define how pixels are operated). Flipper still contains a fixed-function GPU, however, by including components such as the TEV unit, one could argue that Nintendo provided their own shader-like solution.
I guess one of the best examples of games that exploited this new capability is **The Legend of Zelda: Wind Waker** which implements a unique colour/lighting technique known as **Cel shading** to make its textures look _cartoonish_.
### Video output system
The video signal outputs a resolution of up to 640x480 pixels (or 768×576 px in PAL) with up to 16.7 million colours (24-bit depth). Additionally, the system could broadcast its signal in **progressive mode** (which has a clearer image, but not every TV may have supported it during that time).
The XFB can have multiple dimensions, so for compatibility reasons, the Video interface will try its best to display the frame by re-sampling the XFB to fit the TV screen based on the region.
### Connections
The console included not one, but two video output connectors:
[![Image](https://www.copetti.org/images/consoles/gamecube/av_photo.39b45a5cae0412db951695f164ee763d675ea6d804dd752b37705938c1f7f546.jpg)](https://www.copetti.org/images/consoles/gamecube/av_photo.39b45a5cae0412db951695f164ee763d675ea6d804dd752b37705938c1f7f546.jpg)A/V Connections on the back.
  * One named **Analog A/V** which is actually the good-old [Multi Out](https://www.copetti.org/writings/consoles/super-nintendo/#a-convenient-video-out). This is the most popular one.
    * The PAL version of this console doesn’t carry S-Video and the NTSC one doesn’t provide RGB (bummer!).
  * Another one called **Digital A/V** which sends audio and video in digital form (similarly to HDMI nowadays but using a completely different protocol!).
    * Nintendo released a component cable set that connected to this socket. The same plug incorporated a video DAC and encoder to convert the digital signal into YPbPr (optimal quality).
    * The cable was sold as an extra accessory and now is considered some sort of a relic!


* * *
## Audio
Nintendo finally delivered some dedicated audio circuitry to offload the huge task from the CPU-GPU and provide richer sounds. Their new solution is an independent **Digital Signal Processor** or ‘DSP’ manufactured by **Macronix** running inside Flipper.
The DSP’s job consists of performing different operations over our raw audio data (e.g. volume changes, sample rate conversion, 3D sound effects, filtering, echo, reverb, etc) and then output a 2-channel PCM signal. It doesn’t work alone however, the DSP delivers audio with the help of other components.
Its first companion is the **Audio Interface** (AI), a 16-bit stereo digital-to-analogue converter responsible for sending the final sample through the audio signal that ends on the TV. The AI can only process 32 bytes of audio data every 0.25ms, so if we take into account that each sound sample weights 2 bytes and we need two to create stereo sound, the AI will be able to mix up to eight stereo samples with up to 32 kHz of sampling rate, _sound_!
Finally, we have the **Audio RAM** (ARAM) block, which is a large (16 MB) but very slow spare memory that can be used to store raw sound data. There’s quite a lot of space, so the GPU can also use it to store additional material (like textures). The CPU doesn’t have direct access to this memory so it will resort to DMA to move content around.
For better or worse, the DSP is programmable with the use of microcode ([yikes](https://www.copetti.org/writings/consoles/nintendo-64/#audio)), but fear not, as the official SDK already bundles a general-purpose microcode that almost every game used, except on the console’s boot sequence and some Nintendo games (_how convenient_ , as Nintendo didn’t document the DSP, so only they know how to program it).
That being said, the process of generating sound works as follows [[22]](https://www.copetti.org/writings/consoles/gamecube#bib:audio-bourdon):
  1. CPU commands DMA to move raw samples to ARAM.
  2. CPU sends a list of commands that instruct how the DSP should operate these samples. In other words, it uploads the microcode program (only one is officially available for developers).
  3. DSP fetches samples from ARAM, applies the required operations and mixes them into two channels. Finally, it stores the resulting data on RAM.
  4. AI fetches processed samples from RAM and outputs them through the audio signal.


### Compression and freedom
While we’ve already reached the _sampling age_ and we are not locked to specific waveforms anymore, the new sound system is still a huge improvement. For starters, the saga of forced [music sequencing](https://www.copetti.org/writings/consoles/nintendo-64/#audio) is gone for good. The system can now stream pre-produced music to the audio endpoint without problems, much like what the [Saturn](https://www.copetti.org/writings/consoles/sega-saturn/#audio) and [PS1](https://www.copetti.org/writings/consoles/playstation/#audio) accomplished years ago.
Let me show you an example using two games, one released for the Nintendo 64 and its sequel released for the GameCube. Both have different music scores but the context (enemy battle) is the same. Take a look at how both tracks differ in sound quality, taking into account the design of each system (shared vs dedicated).
No support for video.Paper Mario (2000) for the N64.  
Sequenced on the fly by the RSP. No support for video.Paper Mario: The Thousand-Year Door (2004) for the GC.  
Streamed to the DSP.
_As you can hear_ , the DSP finally gave music composers the flexibility and richness they always asked for.
#### Additional material
For a more direct side-by-side comparison, I’ve prepared this interactive widget that shows how composers ended up adapting their arrangements for the GameCube and its predecessor. Here, the same upbeat score is utilised for a Nintendo 64 title and a GameCube one, and the resulting comparison allows me to demonstrate (once again) the technical advantages of the GameCube’s DSP.
Nintendo 64 | GameCube  
---|---  
No support for audio. No support for audio.  
Tap to enable interaction  
**Nintendo 64:** Kirby 64: The Crystal Shards (2000).  
**GameCube:** Kirby Air Ride (2003).
Now, to visualise what’s happening behind each track, here are the two respective spectrograms. Before I start, if you are not familiar with these kinds of charts, I recommend reading my previous NES article, in particular the [audio section](https://www.copetti.org/writings/consoles/nes/#audio) (where I introduced them).
[![Image](https://www.copetti.org/images/consoles/gamecube/spectrograms/kirbycrystal_n64.382830b34024586b5cfcc1e5d2c70f3ae6700f9c678051960b7cbb2a19568274.png)](https://www.copetti.org/images/consoles/gamecube/spectrograms/kirbycrystal_n64.382830b34024586b5cfcc1e5d2c70f3ae6700f9c678051960b7cbb2a19568274.png)Spectrogram of the PCM channel in Kirby 64: The Crystal Shards (2000).[![Image](https://www.copetti.org/images/consoles/gamecube/spectrograms/kirbyair_gc.d98dc788c6546c52d322e597b5435b4d5889cc6c2ecb750094d3f12b637d2b4e.png)](https://www.copetti.org/images/consoles/gamecube/spectrograms/kirbyair_gc.d98dc788c6546c52d322e597b5435b4d5889cc6c2ecb750094d3f12b637d2b4e.png)Spectrogram of the PCM channel in Kirby Air Ride (2003)
To be fair, mixed tracks are difficult to decompose in a spectrogram, but I believe I can attempt to deduce some patterns from it.
To begin with, almost all the frequency spectrum is being evenly utilised in the GameCube track, which may be attributed to the additional instruments used for accompaniment (which add harmonics and therefore fill more areas on the chart).
Finally, the amplitudes on the GameCube spectrogram look more uniformly distributed. In other words, the volume of each instrument is differently balanced and includes effects like reverb. I’m guessing the latter is what the composer originally intended while producing this score, and these types of controls are possible by the fact that the GameCube supports audio streaming. Thus, composers can use any tool of choice to sequence and mix their music, as opposed to strictly depending on the console (and its limitations) to sequence and mix at runtime.
I wouldn’t say that the Nintendo 64 is completely incapable of producing the same result. However, one thing for sure is that, in the world of the Nintendo 64, every single audio function costs extra cycles and/or memory, and this can have an impact on other areas of the game. Hence the need to ration resources. On the other hand, with the GameCube’s support for large samples, one can just stream the full produced score altogether.
* * *
## I/O
It seems that this generation is putting a lot of work into expandability and accessories, the GameCube included a couple of new interesting ports, although some of them remained unused.
### Internal I/O
[![Image](https://www.copetti.org/images/consoles/gamecube/_diagrams/main.b3ccdddb9a7b28e695ebab31ebab7debf79947d8ae681181f690ee5a2768854d.png)](https://www.copetti.org/images/consoles/gamecube/_diagrams/main.b3ccdddb9a7b28e695ebab31ebab7debf79947d8ae681181f690ee5a2768854d.png)Main diagram of the GameCube’s architecture. In there, we find the ‘Northbridge’ which controls most of the I/O.
Flipper is in charge of interfacing the CPU with the rest of the components so, apart from including sound and graphics circuitry, it also provides a collection of hardware named **Northbridge** that is composed of [[23]](https://www.copetti.org/writings/consoles/gamecube#bib:cpu-tree):
  * **Audio Interface** or ‘AI’: Connects the Audio Encoder.
  * **Video Interface** or ‘VI’: Connects the Video Encoder.
  * **Processor Interface** ‘PI’: Connects the CPU (Gekko).
  * **Disk Interface** or ’DI: Connects the DVD controller, which can be considered an independent computer per se.
  * **Serial Interface** or ‘SI’: Connects four possible controllers using a proprietary serial protocol.
  * **External Interface** or ‘EXI’: Connects the external accessories (more explained below), Memory Card and the IPL BIOS along with the Real-Time Clock or ‘RTC’. It uses an SPI-like protocol to connect these devices using only one serial node.


Each interface exposes a set of registers to alter some of its behaviour.
### Optional I/O
On the bottom of the GameCube’s case, you’ll find two external sockets to connect some widgets.
  * [Covered](https://www.copetti.org/writings/consoles/gamecube#nestedtab-1-1-covered)
  * [Uncovered](https://www.copetti.org/writings/consoles/gamecube#nestedtab-1-2-uncovered)

[![Image](https://www.copetti.org/images/consoles/gamecube/accessories_covered.f94a964025baece7ac149d6abbf11e2650b8d7a4e51405ff3a6c374ed12513d2.jpg)](https://www.copetti.org/images/consoles/gamecube/accessories_covered.f94a964025baece7ac149d6abbf11e2650b8d7a4e51405ff3a6c374ed12513d2.jpg)Covered accessory slots on the bottom of the case.[![Image](https://www.copetti.org/images/consoles/gamecube/accessories.e0ead31d7fee68588f51b99dc275c3c4c90abbfa6371ac4043d62a0d09d96d32.jpg)](https://www.copetti.org/images/consoles/gamecube/accessories.e0ead31d7fee68588f51b99dc275c3c4c90abbfa6371ac4043d62a0d09d96d32.jpg)Uncovered accessory slots on the bottom of the case.
Both are technically identical (serial bus running at 32 MHz), yet they are presented with a distinct external shape to accommodate different accessories:
  * **Serial Port 1** : Nintendo shipped Modem and Broadband adapters for this slot.
  * **Serial Port 2** : No public accessory shipped using this port, but you may find some third-parties accessories that provided debugging tools.


These ports are operated on the EXI stack.
### Unusual I/O
You’ll notice I still haven’t mentioned another available socket found next to the serial ports: The **Parallel Port**. This port happens to be much faster (8-bit at 80 MHz vs 1-bit at 32 MHz) which may be the reason Nintendo called it **Hi-Speed Port**. But the most unusual part is that this port is not interfaced through EXI, but through ARAM!
The only official accessory known to date is the famous **Game Boy Player** which plugged in as an extra floor under the GameCube, it contained the necessary hardware to natively play [Game Boy](https://www.copetti.org/writings/consoles/game-boy/) and [Game Boy Advance](https://www.copetti.org/writings/consoles/game-boy-advance/) games. The Player works by doing all the heavy work itself and then sending the results (frames and audio data) to ARAM which the GameCube forwards to the respective components for display/sound.
### Consistent design
I found it worth pointing out that no matter how many accessories you connect, the console will always keep its cubic shape (or at least attempt to).
* * *
## Operating System
Upon turning on the console, the CPU will start loading an operating system called **Dolphin OS** found on the BIOS/IPL chip, this is a very minimal OS that will take care of initialising the hardware and providing some convenient system calls and global variables for games to use. Games developed using the official SDK will implicitly execute these calls during low-level operations.
[![Image](https://www.copetti.org/images/consoles/gamecube/ipl/splash.b0866feda215172342079bef7110e1ec8312711bbb9b351a81e9e9242d48fe76.png)](https://www.copetti.org/images/consoles/gamecube/ipl/splash.b0866feda215172342079bef7110e1ec8312711bbb9b351a81e9e9242d48fe76.png)The official logo, shown after the boot animation finishes.
### Splash and shell
After finishing the boot process, the OS will load a small program _unofficially_ called **Main Menu**.
  * [Menu](https://www.copetti.org/writings/consoles/gamecube#nestedtab-2-1-menu)
  * [Clock](https://www.copetti.org/writings/consoles/gamecube#nestedtab-2-2-clock)
  * [Options](https://www.copetti.org/writings/consoles/gamecube#nestedtab-2-3-options)

[![Image](https://www.copetti.org/images/consoles/gamecube/ipl/menu.755a22d05e3492f78c5b1f7a07ec887d55bfb87a72b5f27eb65d1ac946e76b9a.png)](https://www.copetti.org/images/consoles/gamecube/ipl/menu.755a22d05e3492f78c5b1f7a07ec887d55bfb87a72b5f27eb65d1ac946e76b9a.png)Main Menu with multiple settings available.[![Image](https://www.copetti.org/images/consoles/gamecube/ipl/clock.586de3c1a748f4482f1aac2bd8c37c642aa0e70f6fc6faa320b462e4fd71ef19.png)](https://www.copetti.org/images/consoles/gamecube/ipl/clock.586de3c1a748f4482f1aac2bd8c37c642aa0e70f6fc6faa320b462e4fd71ef19.png)Clock settings.[![Image](https://www.copetti.org/images/consoles/gamecube/ipl/sound.1aae5d16daf0aa8a1bdd4a4619ca51eb5aa5f162318b8759c3ab1dcc71f8d4b5.png)](https://www.copetti.org/images/consoles/gamecube/ipl/sound.1aae5d16daf0aa8a1bdd4a4619ca51eb5aa5f162318b8759c3ab1dcc71f8d4b5.png)Sound settings.
This program is responsible for displaying the famous splash animation (the wee cube drawing a GameCube logo) and loading the game if there is one inserted. In the absence of a _valid_ game, it will then provide a simple cube-shaped menu with various options to choose from:
  * Change Date and Clock.
  * Load the game from the DVD reader.
  * Manage saves on any Memory Card.
  * Change sound settings and screen position.


* * *
## Games
Nintendo provided developers with lots of tools to assist (and encourage) the development of games for their console [[24]](https://www.copetti.org/writings/consoles/gamecube#bib:games-sdk):
  * **Dolphin SDK** : The official set of APIs and useful libraries. This includes the **GX** library in charge of programming Flipper’s GPU.
  * **C** and **C++** Compilers.
  * **Debuggers** and **Testers** : Meant to be used with an official Dev Kit.
  * **Cygnus** : Now known as ‘Cygwin’, it’s basically used to replicate the UNIX environment on Windows.
  * **CodeWarrior** : A de-facto IDE _back in the days_.
  * Various **assistance tools** such as MusyX, Texture editors, Display Lists exporters, USB programmers, etc.
  * Tons and tons of **documentation**! (available in PDF and HTML)


### Specialised hardware
Apart from the software, the company supplied different hardware kits (which range in price) before and after the console was publicly released.
Probably the most popular one worth mentioning is the **Dolphin Development Hardware** or ‘DDH’ which consisted of a PC-like tower containing some of the GameCube’s I/O and lots of dev-assisting hardware [[25]](https://www.copetti.org/writings/consoles/gamecube#bib:games-devstuff), it was mainly used as a debugging station while the game was being developed on a Windows PC.
### Medium
Games are loaded from a proprietary disc called **miniDVD** , it’s almost half the size of a traditional DVD disc and can hold up to 1.4 GB of data.
As an interesting fact, the disc reader operates in a **Constant Angular Velocity** or ‘CAV’ meaning that its data will be read at a faster rate if its found in the outer area of the disc (3.125MB/s) and slower if it’s found in the inner area (2MB/s). This differs from **Constant Linear Velocity** systems (used by traditional CD/DVD readers) where the effects are the opposite.
Game saves are stored in a proprietary external accessory called **Memory Card** and there are enough slots for two of them.
### Unusual controllers
Nintendo shipped an accessory known as the **GameBoy Link Cable** which plugged a [Game Boy Advance](https://www.copetti.org/writings/consoles/game-boy-advance/) into the GC controller port, so games could upload small programs to the GBA and treat it as a special controller. This interesting feature enabled unique interactions and content in some games.
### Online Platform
Well, unlike [the competition](https://www.copetti.org/writings/consoles/dreamcast/), not only did Nintendo require users to buy extra accessories to access online content, but they also didn’t deploy any internet service that publishers could rely on [[26]](https://www.copetti.org/writings/consoles/gamecube#bib:games-online), making developers solely responsible for providing the necessary internet infrastructure.
As a result, while online gaming was a possible feature, it didn’t get widely adopted and only a tiny amount of games made use of this.
* * *
## Anti-Piracy & Homebrew
Nintendo has been in this game for quite some time, so it’s no news that they included security mechanisms to prevent running unauthorised software or games from a different region. Furthermore, due to the new range of I/O that the GameCube provides, the attack surface got significantly larger.
### Security mechanisms
We can organise them into these areas:
  * [DVD controller](https://www.copetti.org/writings/consoles/gamecube#tab-5-1-dvd-controller)
  * [IPL and EXI](https://www.copetti.org/writings/consoles/gamecube#tab-5-2-ipl-and-exi)
  * [Honourable Mention](https://www.copetti.org/writings/consoles/gamecube#tab-5-3-honourable-mention)


#### DVD controller
Even though this is the first Nintendo console to use the disc medium, attempting to play pirated copies of games just wasn’t going to be easy. The miniDVD is protected by using proprietary bar codes on the inner side of the disc, in addition to having its data encrypted. The validation and decryption process works seamlessly: The miniDVD controller takes care of it while the system is limited to only requesting the data.
The hardware composing the DVD reader can be imagined as a fortress wall which is only accessed using a series of commands, the miniDVD controller features a proprietary CPU that will take care of deciding if the inserted disc is genuine or not, and if it’s not, no command issued by the main CPU will convince to read it otherwise.
**Defeat** : As with any other cat-and-mouse game, it was just a matter of time before third-party companies successfully reverse-engineered the controller to build mod-chips that could trick the reader. But bear in mind that no mod-chip will make this console magically fit a conventional CD/DVD without physically altering the case!
« Previous [Next »](https://www.copetti.org/writings/consoles/gamecube#tab-5-2-ipl-and-exi)
#### IPL and EXI
Another possible path of exploitation consists of using the external I/O available to load Homebrew programs. Although, without cracking the DVD reader first, the only other option available is to try to take control of the first program that the GameCube loads, and that is… The IPL.
That means that by reversing engineering the BIOS and replacing the chip with a modified one, one would be able to run, let’s say, a file reader, and from there execute programs received from the accessory ports (assuming the additional hardware is plugged in).
Be as it may, the IPL chip is encrypted using XOR conditionals and a Cipher-text [[27]](https://www.copetti.org/writings/consoles/gamecube#bib:anti_piracy-ipl), making it ‘impossible’ to reverse engineer.
**Defeat** : Hackers eventually discovered that the hardware that handles the decryption of the IPL contained a bug that enabled them to capture the Cipher-text used [[28]](https://www.copetti.org/writings/consoles/gamecube#bib:anti_piracy-steil). With this, another ROM could be constructed and encrypted with the same cypher so the GameCube boots it as its own!
As if that wasn’t enough, hackers also found new methods to trick the miniDVD reader into loading conventional DVDs.
[« Previous](https://www.copetti.org/writings/consoles/gamecube#tab-5-1-dvd-controller) [Next »](https://www.copetti.org/writings/consoles/gamecube#tab-5-3-honourable-mention)
#### Honourable Mention
Before those two mechanisms were discovered, there was actually a much simpler way of loading arbitrary code without any modification whatsoever. This method consisted of **hijacking the online protocol**.
Some games like _Phantasy Star Online_ implemented their own online functionality, which could be updated by downloading an updated executable (DOL file) from the company’s servers, and the latter didn’t implement any security in its protocol. So, as you can see, this was a man-in-the-middle attack waiting to happen…
Long story short, by spoofing a fake server the GameCube would just download (and execute) whatever DOL you could provide. That means hackers only needed the original game and the broadband adapter. This technique is known as **PSOload** [[29]](https://www.copetti.org/writings/consoles/gamecube#bib:anti_piracy-psoload).
[« Previous](https://www.copetti.org/writings/consoles/gamecube#tab-5-2-ipl-and-exi) Next »
* * *
## That’s all folks
[![Image](https://www.copetti.org/images/consoles/gamecube/my_gamecube.549b48d925a376192076e81d1c4d7acdf57280a3b55838a5b0295b96d838009b.jpeg)](https://www.copetti.org/images/consoles/gamecube/my_gamecube.549b48d925a376192076e81d1c4d7acdf57280a3b55838a5b0295b96d838009b.jpeg)My old GameCube recently rescued from the attic. I only needed the controller for the Wii (back then it was cheaper to buy the whole second-hand lot!).
Well, this is it, the **10 th article**!
I really tried to set a rough limit on the length of this article but you have to understand, technology has gotten _so complex_ that if I accidentally skip anything important, the whole topic gets impossible to follow.
Anyway, I’d like to thank the #dolphin-dev IRC community for helping me understand the complicated pipeline of Flipper’s GPU, these guys have been developing the GameCube emulator for quite some years now and it’s really impressive how much they had to put up with.
And finally, please consider [contributing](https://www.copetti.org/support/) if you found it an interesting read. I strive to make it as complete as I can, and in the process, I forget how much time it’s suddenly costing me, I find it a good investment nonetheless.
Until next time!  
Rodrigo.
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
- Any IPL mod (?)
### Acquired tools used
- (While ago) Gamecube with controller (£20) and some games (if I remember correctly, no more than £20...)
```

Alternatively, you can help out by [suggesting changes](https://github.com/flipacholas/Architecture-of-consoles) and/or [adding translations](https://github.com/flipacholas/Architecture-of-consoles).
* * *
## Copyright and permissions
This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). You may use it for your work at no cost, even for commercial purposes. But you have to respect the license and reference the article properly. Please take a look at the following guidelines and permissions:
Article information and referencing
For any referencing style, you can use the following information:
  * **Title of article** : GameCube Architecture - A Practical Analysis
  * **Author** : Rodrigo Copetti
  * **URL** : <https://www.copetti.org/writings/consoles/gamecube/>
  * **Date of publication** : November 19, 2019
  * **Last modified** : August 17, 2025


For instance, to use with BibTeX:
```
@misc{copetti-gamecube,
    url = {https://www.copetti.org/writings/consoles/gamecube/},
    title = {GameCube Architecture - A Practical Analysis},
    author = {Rodrigo Copetti},
    year = {2019}
}

```

or a IEEE style citation:
```
[1]R. Copetti, "GameCube Architecture - A Practical Analysis", Copetti.org, 2019. [Online]. Available: https://www.copetti.org/writings/consoles/gamecube/. [Accessed: day- month- year].

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
  * gc-forever.com, [PSOLoad](https://www.gc-forever.com/wiki/index.php?title=PSOload). [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:29)
  * ogamespec, [Gc-ipl](https://github.com/ogamespec/gc-ipl). Github. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:27)
  * Felix Domke, Michael Steil, Rob Reilink, [GameCube hacking](https://c3media.vsos.ethz.ch/congress/2004/papers/208%20GameCube%20Hacking.pdf). 21st Chaos Communication Congress. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:28)


### Audio
  * Pierre Bourdon, [Emulating the gamecube audio processing in dolphin](https://blog.lse.epita.fr/articles/38-emulating-the-gamecube-audio-processing-in-dolphin.html). [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:22)


### CPU
  * groepaz/hitmen, [Yet another gamecube documentation](http://hitmen.c02.at/files/yagcd/yagcd/). [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:15)
  * Andrei Shestakov, [Hardware acronyms](https://www.gc-forever.com/wiki/index.php?title=Hardware_Acronyms). GC-Forever Wiki.
  * The Linux Kernel Archives, [Nintendo GameCube device tree](https://www.kernel.org/doc/Documentation/devicetree/bindings/powerpc/nintendo/gamecube.txt). [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:23)
  * IBM, IBM PowerPC 750CX/750CXe RISC - microprocessor user’s manual. 2001. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:11)
  * IBM, IBM gekko RISC microprocessor user’s manual. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:13)
  * Anand Lal Shimpi, [Hardware behind the consoles - part II: Nintendo’s GameCube](https://www.anandtech.com/show/858/2). AnandTech.
  * GDC Vault, [Nintendo GameCube programming 101](https://www.gdcvault.com/play/1022547/Nintendo-GameCube-Programming). 2002. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:18)
  * Jon Stokes, [PowerPC on apple: An architectural history, part II](https://archive.ph/vb5cN). Ars Technica. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:12)
  * MayImilae and JMC47, [Booting the final GameCube game](https://dolphin-emu.org/blog/2016/09/06/booting-the-final-gc-game/). Dolphin Emulator. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:16)
  * Keith Diefendorff, [PowerPC G4 gains velocity](https://www.ardent-tool.com/CPU/docs/MPR/19991025/131402.pdf). Microprocessor Report, 1999.
  * Keith Diefendorff, [PowerPC 601 microprocessor, lecture by keith diefendorff](https://www.youtube.com/watch?v=BRoS_m1g1_Q). Youtube, 1993. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:4)
  * The Paranoid of Paradox, [The unpopular successor - the PowerPC](https://dhs.nu/misc.php?t=special&feature=ppc). Dead Hackers Society, 2007. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:7)
  * IBM - Motorola, PowerPC 603 ™ RISC microprocessor hardware specifications. 1997. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:8)
  * HandWiki, [IBM POWER microprocessors](https://encyclopedia.pub/entry/35950). 2022. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:2)
  * Gregory F. Grohosk, Machine organization of the IBM RISC system/6000 processor. 1990. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:3)
  * Brian Case, [IBM delivers first PowerPC microprocessor](https://websrv.cecs.uci.edu/~papers/mpr/MPR/ARTICLES/061401.pdf). 1992. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:5)
  * IBM - Motorola, PowerPC 601 ™ RISC microprocessor user’s manual. 1997. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:6)
  * IBM - Motorola, PowerPC 604™ RISC microprocessor hardware specifications. 1997. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:9)
  * IBM, PowerPC 403GA 32-bit RISC embedded controller. 1998. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:10)


### Games
  * Dragoon, [Dolphin SDK, compilers (and cracks), tools and more](http://web.archive.org/web/20191119113112/https://assemblergames.com/threads/dolphin-sdk-compilers-and-cracks-tools-and-more.69956/). ASSEMblergames.com. Archived. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:24)
  * pstrick1, [Comprehensive list of gamecube dev stuff](http://web.archive.org/web/20191113075154/https://assemblergames.com/threads/comprehensive-list-of-gamecube-dev-stuff.29487/). Archived. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:25)
  * Wikipedia contributors, [GameCube online functionality — Wikipedia, the free encyclopedia](https://en.wikipedia.org/w/index.php?title=GameCube_online_functionality&oldid=918543830) (\\[Online; accessed 10-July-2022\\]). 2019. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:26)


### Graphics
  * Howard Cheng, [NINTENDO GAMECUBE: The ultimate video game machine](https://cubemedia.ign.com/media/news/documents/embeddedforumkeynote.pdf). [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:17)
  * Brian Neal, [Game consoles: A look ahead](https://aceshardware.com/pdfs/AcesHardware-60000286.pdf). Ace's Hardware. Archived.
  * devkitpro.org, [Libogc/GX](https://devkitpro.org/wiki/libogc/GX).
  * Tim Van Hook, [Implementation of the ATI flipper chip](http://www.graphics.stanford.edu/courses/cs448a-01-fall/lectures/tvh/tvh.2up.pdf). ATI Technologies. Standford Computeer Graphics Laboratory.
  * Omar Shehata, [A beginner’s guide to coding graphics shaders](https://gamedevelopment.tutsplus.com/tutorials/a-beginners-guide-to-coding-graphics-shaders--cms-23313).
  * Dave Salvator, [ExtremeTech 3D pipeline tutorial](https://www.extremetech.com/computing/49076-extremetech-3d-pipeline-tutorial).
  * NWR Staff, [NGC graphical abilities](http://www.nintendoworldreport.com/guide/1786/gamecube-faq-ngc-graphical-abilities). Nintendo World Report. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:19)
  * MayImilae and JMC47, [To the screen with hybrid XFB](https://dolphin-emu.org/blog/2017/11/19/hybridxfb/). Dolphin Emulator. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:21)
  * MayImilae and JMC47, [Ubershaders: A ridiculous solution to an impossible problem](https://dolphin-emu.org/blog/2017/07/30/ubershaders/). Dolphin Emulator. [↩︎](https://www.copetti.org/writings/consoles/gamecube#bibref:20)


### Photography
  * Evan Amos, [The vanamo online game museum](https://commons.wikimedia.org/wiki/User:Evan-Amos).
  * Rodrigo Copetti (Me), [Diagrams, casual photos, screenshots and videos](https://www.copetti.org/).


* * *
## Changelog
It’s always nice to keep a record of changes. For a complete report, you can check the [commit log](https://github.com/flipacholas/Architecture-of-consoles/commits/master/articles/gamecube.Rmd.md). Alternatively, here’s a simplified list:
```
### 2025-04-20
- Added photograph of IBM POWER board after a quick visit to The Computer History Museum (Mountain View, California) in March 2025.
### 2025-01-06
- Added history of PowerPC (from the 808 to the 970/G5)
### 2023-02-11
- Added additional material to the audio section
### 2022-12-04
- Corrected ambiguity between Flipper (the SoC) and its internal GPU. See https://github.com/flipacholas/Architecture-of-consoles/issues/150 and https://github.com/flipacholas/Architecture-of-consoles/issues/151 (thanks @phire, @Pokechu22, @Masamune3210 and @aboood40091)
### 2021-06-20
- Added 32 vs 64 bits paragraph
- Expanded audio section
### 2021-05-15
- Added MMU+ARAM section
- Added memory layout diagram
- Improved 'Sources' structure
### 2020-02-26
- Added mention on anisotropic filtering
### 2020-01-09
- Improved the write gather pipe explanation
### 2019-11-22
- Corrections and more info added, thanks @phire from #dolphin-dev and /r/gamecube !
### 2019-11-20
- Corrections here and there
### 2019-11-19
- Public release!
```

* * *
[« Game Boy Advance Architecture](https://www.copetti.org/writings/consoles/game-boy-advance/) [Xbox Architecture »](https://www.copetti.org/writings/consoles/xbox/)
![Rodrigo Copetti](https://www.copetti.org/favicon/favicon.png)
### Rodrigo Copetti
I hope you have enjoyed this article! If you want to know more about the author [tap here](https://www.copetti.org/about/) and if you would like to support him [tap here](https://www.copetti.org/support/) instead
[Tweet ](https://twitter.com/intent/tweet?text=GameCube%20Architecture%20%7c%20A%20Practical%20Analysis%20https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fgamecube%2f)[Share ](javascript:void\(0\))[Share ](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fgamecube%2f&title=GameCube%20Architecture%20%7c%20A%20Practical%20Analysis&summary=An%20in-depth%20analysis%20that%20explains%20how%20this%20console%20works%20internally&source=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fgamecube%2f)[Share](https://reddit.com/submit?url=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fgamecube%2f&title=GameCube%20Architecture%20%7c%20A%20Practical%20Analysis)
[Switch to classic edition](https://classic.copetti.org/writings/consoles/gamecube/)
Rodrigo Copetti © 2025 [](https://www.copetti.org/index.xml)
[About the website and its content](https://www.copetti.org/disclaimer/)
rsslinkedintwitterblueskygithub facebookreddit
