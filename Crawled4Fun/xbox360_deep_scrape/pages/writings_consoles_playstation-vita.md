# PlayStation Vita Architecture (Part 1) | A Practical Analysis

**Source:** https://www.copetti.org/writings/consoles/playstation-vita

[Home](https://www.copetti.org/)
[Consoles](https://www.copetti.org/writings/consoles/)
[About](https://www.copetti.org/about/)
[Support](https://www.copetti.org/support/)
# PlayStation Vita Architecture (Part 1)
## A practical analysis by Rodrigo Copetti
[](https://github.com/flipacholas/Architecture-of-consoles)[](https://crowdin.com/project/architecture-of-consoles)[](https://www.copetti.org/writings/consoles/materials/readings/)[](https://www.copetti.org/writings/consoles/playstation-vita)
If you use accessibility tools or old browsers, [switch to the ‘classic’ edition](https://classic.copetti.org/writings/consoles/playstation-vita/).
🇬🇧 - English 👋 - Add translation
* * *
Book edition
[![eBook edition](https://www.copetti.org/images/consoles/_covers/en/playstation-vita_hu_adaaaa270f30365d.jpg)](https://www.copetti.org/writings/consoles/materials/book/)
Upon completion, this article will be published in many bookstores for the benefit of offline readers. The eBook will be DRM-free, while the printed edition will compile multiple articles and feature original photography at full resolution.
Meanwhile, you can find existing printed compilations [here](https://www.amazon.com/dp/B0F4P5RB25?binding=paperback), and individual eBooks at [Amazon Kindle](https://www.amazon.com/dp/B0B5VM3NHS), [Apple Books](https://books.apple.com/us/author/rodrigo-copetti/id1632545359?see-all=books), [Kobo](https://www.kobo.com/us/en/search?query=Architecture+of+Consoles%3a+A+Practical+Analysis&fcsearchfield=Series&seriesId=7e46f843-4aee-53b4-97c2-82782e951af5) and [other stores](https://www.copetti.org/writings/consoles/materials/book/). The proceeds support the improvement of current articles and the development of new ones.
For more information, please take a look at [here](https://www.copetti.org/writings/consoles/materials/book/).
* * *
Table of Contents
  1. [Supporting imagery](https://www.copetti.org/writings/consoles/playstation-vita#imagery)
  2. [A quick introduction](https://www.copetti.org/writings/consoles/playstation-vita#a-quick-introduction)
    1. [A new publishing model](https://www.copetti.org/writings/consoles/playstation-vita#a-new-publishing-model)
  3. [Models and variants](https://www.copetti.org/writings/consoles/playstation-vita#models-and-variants)
  4. [CPU](https://www.copetti.org/writings/consoles/playstation-vita#cpu)
    1. [The main CPU](https://www.copetti.org/writings/consoles/playstation-vita#the-main-cpu)
      1. [Continued history](https://www.copetti.org/writings/consoles/playstation-vita#continued-history)
        1. [The Cortex line-up](https://www.copetti.org/writings/consoles/playstation-vita#the-cortex-line-up)
        2. [More news](https://www.copetti.org/writings/consoles/playstation-vita#more-news)
      2. [The core](https://www.copetti.org/writings/consoles/playstation-vita#the-core)
      3. [The grown-up ISA](https://www.copetti.org/writings/consoles/playstation-vita#the-grown-up-isa)
        1. [A quick glance](https://www.copetti.org/writings/consoles/playstation-vita#tab-1-1-a-quick-glance)
        2. [Overshadowing features](https://www.copetti.org/writings/consoles/playstation-vita#tab-1-2-overshadowing-features)
        3. [More accelerators](https://www.copetti.org/writings/consoles/playstation-vita#more-accelerators)
    2. [The master bus (or buses)](https://www.copetti.org/writings/consoles/playstation-vita#the-master-bus-or-buses)
    3. [Envisioning the future](https://www.copetti.org/writings/consoles/playstation-vita#envisioning-the-future)
    4. [The new media coprocessor](https://www.copetti.org/writings/consoles/playstation-vita#the-new-media-coprocessor)
      1. [Architecture of Venezia](https://www.copetti.org/writings/consoles/playstation-vita#tab-2-1-architecture-of-venezia)
      2. [A curious rendition](https://www.copetti.org/writings/consoles/playstation-vita#tab-2-2-a-curious-rendition)
    5. [Memory available](https://www.copetti.org/writings/consoles/playstation-vita#memory-available)
      1. [Main memory](https://www.copetti.org/writings/consoles/playstation-vita#main-memory)
      2. [Other memory](https://www.copetti.org/writings/consoles/playstation-vita#other-memory)
    6. [One last CPU](https://www.copetti.org/writings/consoles/playstation-vita#one-last-cpu)
  5. [Next: Graphics](https://www.copetti.org/writings/consoles/playstation-vita#next-graphics)
  6. [Copyright and permissions](https://www.copetti.org/writings/consoles/playstation-vita#referencing)
  7. [Sources / Keep Reading](https://www.copetti.org/writings/consoles/playstation-vita#sources)
  8. [Contributing](https://www.copetti.org/writings/consoles/playstation-vita#contributing)
  9. [Changelog](https://www.copetti.org/writings/consoles/playstation-vita#changelog)


* * *
## Supporting imagery
  * [Model](https://www.copetti.org/writings/consoles/playstation-vita#cover-model)
  * [Motherboard](https://www.copetti.org/writings/consoles/playstation-vita#cover-motherboard)


### Model
  * [Original](https://www.copetti.org/writings/consoles/playstation-vita#cover-model-original)
  * [Slim](https://www.copetti.org/writings/consoles/playstation-vita#cover-model-slim)
  * [TV](https://www.copetti.org/writings/consoles/playstation-vita#cover-model-tv)

[![Original](https://www.copetti.org/images/consoles/psvita/psvita.2359d8f1dec0379a85c91390f6f19870eae50bb233663be55a85dab75b8ec706.png)](https://www.copetti.org/images/consoles/psvita/psvita.2359d8f1dec0379a85c91390f6f19870eae50bb233663be55a85dab75b8ec706.png)The PlayStation Vita (model PCH-1000).  
Released on 17/12/2011 in Japan, 12/02/2012 in America and 22/02/2012 in Europe.[![Slim](https://www.copetti.org/images/consoles/psvita/psvita2.ef145b257ce54a14372f29e1e664cad7e23422aeee2aa5cdc408adc6b9e3cc60.png)](https://www.copetti.org/images/consoles/psvita/psvita2.ef145b257ce54a14372f29e1e664cad7e23422aeee2aa5cdc408adc6b9e3cc60.png)The 'updated' PS Vita (model PCH-2000, a.k.a. 'Slim').  
Released on 10/10/2013 in Japan, 07/02/2014 in Europe and 06/05/2014 in America.[![TV](https://www.copetti.org/images/consoles/psvita/pstv.56fe02a3c4e775ce5ed82886d3a26b32e743a41630484a3712eea93b01b8a13d.png)](https://www.copetti.org/images/consoles/psvita/pstv.56fe02a3c4e775ce5ed82886d3a26b32e743a41630484a3712eea93b01b8a13d.png)The 'consolised' PS Vita (model VTE-1000).  
Released on 14/11/2013 in Japan, 14/10/2014 in America and 14/11/2014 in Europe.
### Motherboard
  * [Original](https://www.copetti.org/writings/consoles/playstation-vita#cover-motherboard-original)
  * [Marked](https://www.copetti.org/writings/consoles/playstation-vita#cover-motherboard-marked)

[![Motherboard](https://www.copetti.org/images/consoles/psvita/motherboard.6d1548d888195ac285bb5f08295337dba51ac54cf2158ac042cf7cf94e928962.png)](https://www.copetti.org/images/consoles/psvita/motherboard.6d1548d888195ac285bb5f08295337dba51ac54cf2158ac042cf7cf94e928962.png)Motherboard  
If you yank off the I/O, it becomes a smartphone.[![Motherboard](https://www.copetti.org/images/consoles/psvita/motherboard_marked.17320d276ee958063b255e28ee3710ab39bcbf8e3be4b98701401e8f874917ee.png)](https://www.copetti.org/images/consoles/psvita/motherboard_marked.17320d276ee958063b255e28ee3710ab39bcbf8e3be4b98701401e8f874917ee.png)Motherboard with important parts labelled
* * *
## A quick introduction
The PSVita is a noteworthy intersection between the video-game establishment and the rapidly evolving mobile sector. Times have changed, and it won’t be easy for Sony as it faces fierce competition from cheap gadgets that do more than just make phone calls.
The new analysis of [this series](https://www.copetti.org/writings/consoles/) dives into the contemporary technology behind Sony’s new delivery. Do expect to find recognisable circuitry - perhaps too familiar. Even so, Sony made clear efforts to steer away from any resemblance to the smartphone market.
### A new publishing model
Until now, my delivery model involved finishing the whole analysis and then publishing a complete article at once. However, as I continue studying the 8th generation, my articles have considerably grown in complexity. They tend to take almost a year to finish, and the review process has become too cumbersome. Thus, for a change, I’d like to try a new phased approach where I publish by sections instead. This will also make the reviewing stage more efficient.
Having said that, let’s start with the first section.
* * *
## Models and variants
As the console sat on store shelves, Sony revisited its product strategy multiple times, leading to three variants of the PSVita being shipped throughout its lifecycle:
  * The **original** PSVita (sometimes called the ‘Fat’ model) is the series debut.
  * The **Slim** revision retains the same architecture, but exchanges the OLED screen for an LCD to reduce costs. Furthermore, it doesn’t offer a 3G-capable variant anymore. It does, however, feature a bigger eMMC chip… only 52 MB larger! For some strange reason, that was enough to provide an internal 1 GB memory card. In any case, I’ll explain more in the ‘Games’ section.
  * The **PlayStation TV** is just a Fat motherboard adapted for the non-portable setting. It also exposes a different set of I/O.


As you can see, the information in this article will easily apply to all three models, although I will dedicate extra paragraphs to talk about the puzzling eMMC changes of the last two variants.
* * *
## CPU
Sony had been an avid adopter of MIPS technology since the original PlayStation. Even at times when SGI/MIPS was losing market share in the late 90s, Sony shipped a [successful product](https://www.copetti.org/writings/consoles/playstation-portable/) carrying MIPS’ [revamped line](https://www.copetti.org/writings/consoles/playstation-portable/#mips-after-the-turn-of-the-century). However, the next decade proved bitter: ARM managed to [monopolise](https://www.copetti.org/writings/consoles/nintendo-ds/#turning-points) the mobile market and MIPS’ adoption only diminished. Thus, Sony ultimately put their faith in an ARM CPU instead, and Toshiba (Sony’s close manufacturing [partner](https://www.copetti.org/writings/consoles/playstation-2/#a-special-order-for-sony)) would now play the role of [ARM licensee](https://www.copetti.org/writings/consoles/game-boy-advance/#tab-1-2-a-new-cpu-venture).
The resulting motherboard only houses a handful of integrated circuits, but they package a mix of designs authored by different companies. The main chip is called **Kermit** [[1]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-kermit) (a name borrowed from ‘The Muppets’), it features the largest amount of circuitry, and it’s where the main CPU resides.
[![Image](https://www.copetti.org/images/consoles/psvita/photos/kermit.eacea19e5654107edd286da36949155f606f9545d2ad9d8820542bb5e36b65b7_hu_22d4b9c0865dc1e7.png)](https://www.copetti.org/images/consoles/psvita/photos/kermit.eacea19e5654107edd286da36949155f606f9545d2ad9d8820542bb5e36b65b7.webp)The Kermit chip in the original PSVita model. This tiny block houses multiple CPUs, GPUs and ~640 MB of RAM… how far we’ve come!
Now, while Kermit is considered a **System-On-Chip** (SoC), it exceptionally manages to combine large amounts of memory and processors within the same package. This is thanks to Toshiba’s **Stacked Chip SoC** (SCS) fabrication model [[2]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-scs). Within it, circuitry is piled on top of others - as opposed to being externally connected side-by-side. The direct consequence is an increase of bandwidth and a reduction of surface footprint, at the cost of a more complex heat dissipation design.
In any case, SCS fabrication enabled Sony and Toshiba to fit cutting-edge technology while maintaining an energy-efficient profile, just look at all the components Kermit houses:
  * The **main CPU** , a quad-core ARM Cortex-A9 MPCore.
  * The **main GPU** , a PowerVR SGX543MP4+ by Imagination Technologies.
  * Many **accelerators** (some proprietary, others off the shelf), including a large DSP, [DMA Controllers](https://www.copetti.org/writings/consoles/playstation/#taking-over-the-cpu) and security blocks (housing hidden ROM space).
  * **Around 640 MB of RAM** (split into multiple types).
  * Last but not least, **legacy PlayStation Portable circuitry** (the [MIPS CPU](https://www.copetti.org/writings/consoles/playstation-portable/#main-cpu) and the [Graphics Engine](https://www.copetti.org/writings/consoles/playstation-portable/#graphics)).


…and throughout this article we’ll take a look at each of those!
### The main CPU
Our new study subject is the **ARM Cortex-A9 MPCore** , a very mature processor from ARM Ltd. 
To make this study captivating and help understand all the technological progress since [my last analysis](https://www.copetti.org/writings/consoles/nintendo-3ds/#cpu) of the ARM11 CPU, I’d like to begin with an overview of the new ‘Cortex’ line. Then, a quick look at the Cortex-A8 (the predecessor of the A9). Finally, the novelties of the Cortex-A9.
#### Continued history
[![Image](https://www.copetti.org/images/consoles/gba/cpu_agb.5718b7d30c573e668823d04f3b2df402e5d74eced59d0aca30219c2171549a56.png)](https://www.copetti.org/images/consoles/gba/cpu_agb.5718b7d30c573e668823d04f3b2df402e5d74eced59d0aca30219c2171549a56.png)The Game Boy Advance housed an ARM7TDMI.[![Image](https://www.copetti.org/images/consoles/nintendods/cpu_ntr.e00a63784a027cf659e3c8d8f61868a1c9708a3f8b3d4b89e533e991218c0efb.jpg)](https://www.copetti.org/images/consoles/nintendods/cpu_ntr.e00a63784a027cf659e3c8d8f61868a1c9708a3f8b3d4b89e533e991218c0efb.jpg)The Nintendo DS housed an ARM946E-S and ARM7TDMI.Past System-on-Chips (SoCs) housing iconic ARM CPUs.
ARM has come a long way since the days of the [Game Boy Advance](https://www.copetti.org/writings/consoles/game-boy-advance/), to recall its significant milestones:
  * The ARM CPU was conceived as a [replacement](https://www.copetti.org/writings/consoles/game-boy-advance/#tab-1-1-the-rise-of-acorn-computers) of the [MOS 6502](https://www.copetti.org/writings/consoles/nes/#cpu) CPU for Acorn’s computers, later reaching maturity thanks to [Apple’s input](https://www.copetti.org/writings/consoles/game-boy-advance/#tab-1-2-a-new-cpu-venture).
  * The [ARM7TDMI](https://www.copetti.org/writings/consoles/game-boy-advance/#the-arm7tdmi) paved the way for success in the embedded market. At the same time, competitors across the pond [chose to avoid any mobile venture](https://www.copetti.org/writings/consoles/playstation-portable/#the-end-of-the-line).
  * The subsequent [StrongARM/ARM9](https://www.copetti.org/writings/consoles/nintendo-ds/#arms-new-territories) line granted the company a spot in the performance sector.
  * [As the competition faded](https://www.copetti.org/writings/consoles/playstation-portable/#the-end-of-the-line), the new [ARM11 line](https://www.copetti.org/writings/consoles/nintendo-3ds/#cpu) demonstrated this CPU could now partake on 3D applications.


The next achievement would become **Cortex** : a new brand carrying a revised instruction set and processor line. This time, ARM would adopt practices traditionally found in the desktop/workstation market, eventually coming heads-to-head with Intel’s x86. Curiously enough, Cortex’s marketing strategy is very similar to Intel’s Pentium, in the sense that the name ‘Cortex’ ultimately becomes an ambiguous term to hide the complicated identifications and variants of all its chips.
##### The Cortex line-up
With the announcement of Cortex as a brand, ARM’s product line diversified into three distinguishable sectors: **industrial** , **performance** and **embedded**. Thus, any Cortex CPU would be fitted into a ‘profile’ (Cortex-R, Cortex-A and Cortex-M, respectively), each targeting one of these markets. For this study, we’ll focus on the **Cortex-A** line, which focused on performance or ‘applications’ (in other words, user devices); and made a profound impact on smartphones.
[![Image](https://www.copetti.org/images/consoles/psvita/cortexa8_phones.fce29b750612bf9558672988bda179ca1b946360bd89775cd85d61b65e454ac1_hu_c614db159d3ceee9.png)](https://www.copetti.org/images/consoles/psvita/cortexa8_phones.fce29b750612bf9558672988bda179ca1b946360bd89775cd85d61b65e454ac1.webp)Some smartphones from the Cortex-A8 generation. From left to right: iPhone 3GS (2009), Nokia N900 (2009), Palm Pre (2009) and Nexus S (2010)
ARM’s first delivery for ‘applications’ was the **Cortex-A8** CPU. It shipped in 2005, but it wasn’t until four years later that smartphones started adopting it. The **iPhone 3GS** , **Motorola Droid** and **Nokia N900** were its debuting flagship carriers. Be as it may, the CPU can’t work by itself, so these devices relied on Samsung and Texas Instruments to package all the necessary modules into a SoC (combining the CPU with the GPU, modem and other I/O).
It’s worth mentioning that the Cortex CPU was also a decisive choice for manufacturers finally making the jump from [Intel’s XScale](https://www.copetti.org/writings/consoles/nintendo-ds/#turning-points), such as RIM and its Blackberry line. On the other side, certain smartphones like the Toshiba TG01 and the HTC HD2 only adopted Cortex’s technology partially (they implement the same instruction set, but its microarchitecture was designed by Qualcomm instead).
Notice that these devices also coincide with a certain time when users considerably changed their attitude towards smartphones: these were initially trusted for trivial tasks such as text messages and e-mail, but now they were starting to provide access to bank accounts, with only a few years behind bringing contactless payments.
##### More news
Along the Cortex-A8 came the **ARMv7** instruction set. This is the continuation of the [ARMv6 ISA](https://www.copetti.org/writings/consoles/nintendo-3ds/#new-dialects) by expanding its multi-processing and SIMD capabilities [[3]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-thomas_v7).
ARMv7 is the longest-living 32-bit ISA from ARM, but also the last one. Its widespread adoption would still be highly [fragmented](https://www.copetti.org/writings/consoles/nintendo-3ds/#and-a-fragmented-distribution), mainly due to the split of Cortex into the aforementioned profiles (spawning different subsets of the ISA), existing adoption of the ARMv6 (i.e. the first Raspberry Pi and Nokia’s Symbian platform only supported ARMv6) and the enlargement of Thumb. To avoid making this topic too dense, I’ve dedicated different sections further down to discuss these.
#### The core
So far I’ve talked about the Cortex-A8, that’s the first Cortex CPU. But the PSVita actually bundles the succeeding CPU, the **Cortex-A9** (unveiled two years later, in 2007). It’s curious to see that this console was just a few months apart from the [Nintendo 3DS](https://www.copetti.org/writings/consoles/nintendo-3ds/), a console designed with horizontal innovation in mind.
Moving on, the full name of the PSVita’s CPU is **ARM Cortex-A9 MPCore**. Overall, this means the CPU is a cluster made of **multiple Cortex-A9 cores** , **four** in this case. It runs at a clock speed of **up to 500 MHz** [[4]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-psdev_cpu), an underwhelming number considering contemporary adopters of the quad-core A9, such as the Samsung Galaxy S III, reached speeds of 1.4 GHz [[5]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-galaxy). It’s possible that battery life was the main priority here. Nevertheless, clock speed is not the only decisive measurement, the inner workings of the CPU are as important.
  * [Cortex-A9](https://www.copetti.org/writings/consoles/playstation-vita#nestedtab-1-1-cortex-a9)
  * [ARM11](https://www.copetti.org/writings/consoles/playstation-vita#nestedtab-1-2-arm11)

[![Image](https://www.copetti.org/images/consoles/psvita/cpu/mpcore_overview.ab927ccdc435c9c320a4cfeb4289d482f001516dd1ef1ecf082c5d9e40d5e658.png)](https://www.copetti.org/images/consoles/psvita/cpu/mpcore_overview.ab927ccdc435c9c320a4cfeb4289d482f001516dd1ef1ecf082c5d9e40d5e658.png)Overview of the PSVita’s Cortex-A9 MPCore CPU. ‘Falcon’ is the codename of the Cortex-A9 core.[![Image](https://www.copetti.org/images/consoles/nintendo3ds/cpu/mpcore_new_overview.73042809fa9f8f34cbea6e462ef0d89128a814b522968e63bb28ae4e3a00b9e1.png)](https://www.copetti.org/images/consoles/nintendo3ds/cpu/mpcore_new_overview.73042809fa9f8f34cbea6e462ef0d89128a814b522968e63bb28ae4e3a00b9e1.png)Here’s the previous quad-core [ARM11 MPCore](https://www.copetti.org/writings/consoles/nintendo-3ds/#cpu), found on the ‘New’ Nintendo 3DS, for comparison purposes.
Speaking of which, the new cores share many characteristics with their predecessor, the Cortex-A8, which includes [[6]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-cortexa8_reference):
  * The next-generation instruction set called **ARMv7-A** , I explain more details further on.
  * **64 KB of L1 cache** which inherently follows the [Harvard architecture](https://www.copetti.org/writings/consoles/nintendo-ds/#arms-new-territories). Consequently, it’s divided into **32 KB for data** and **32 KB for instructions**.
    * Data cache coherency among the cores is automatically handled by the [Snoop Control Unit](https://www.copetti.org/writings/consoles/nintendo-3ds/#tab-1-3-the-axi-bus), previously featured in the ARM11MpCore.
  * **2-issue superscalar** : For the first time, ARM has brought [instruction-level parallelism](https://www.copetti.org/writings/consoles/xbox-360/#an-alternative-solution). This means that, as long as there are no [hazards](https://www.copetti.org/writings/consoles/playstation/#delay-galore), the CPU will try to execute two instructions using two separate pipelines. This increases the amount of instructions executed per clock cycle. [MIPS](https://www.copetti.org/writings/consoles/playstation-2/#tab-1-1-outperforming-success) and [SuperH](https://www.copetti.org/writings/consoles/dreamcast/#the-offering) brought this a decade before, but the two suffered a quick demise, so it’s now ARM’s turn to carry it forward.
  * **Dynamic branch prediction** : The CPU now predicts the execution path by relying on two dedicated buffers while fetching instructions. The first anticipates whether an upcoming instruction will be a branch, and the next buffer maps the previous flow of the program. Finally, the latter is used to predict whether upcoming branches will be taken or not [[7]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-cortexa8_imp).
    * It’s worth mentioning that this unit **only predicts branching instructions** , omitting other optimisation techniques such as [conditionals](https://www.copetti.org/writings/consoles/game-boy-advance/#commanding-the-cpu) or the `IT` instruction… Maybe that’s a hint about the future of the ARM ISA.
  * A [Memory Management Unit](https://www.copetti.org/writings/consoles/nintendo-64/#memory-management) (MMU) with a Translation Lookaside Buffer (TLB). This is already typical on most CPUs.
    * By the way, in the case of the Cortex brand, only the ‘Cortex-A’ profile includes this package. The ‘Cortex-R’ series only bundles an [MPU](https://www.copetti.org/writings/consoles/playstation-portable/#focused-memory-management) (and it’s even optional on some ‘Cortex-M’ models [[8]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-cortexm3)).
  * **TrustZone** : A new security subsystem that adds a dimension to the [privilege levels](https://www.copetti.org/writings/consoles/playstation-portable/#focused-memory-management) of the MMU. It’s implemented on both the hardware level (by segregating components between non-secure and secure groups) and the software level (by executing a secondary and isolated operating system that handles confidential data). The special OS is called **Trusted Execution Environment**. Furthermore, data transfers carry an extra tag to indicate whether they are secure or insecure transactions [[9]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-cortexa_prog).
    * The OS model of TrustZone reminds me of the [isolated SPU of Cell](https://www.copetti.org/writings/consoles/playstation-3/#cells-privileged-security).
  * **NEON Media Processing Engine** (MPE), a new co-processor that carries out vector and floating-point operations. We’ll dive more into it in the next sections.


Now, the Cortex-A9 series (found in the PSVita) improves the original design by applying significant enhancements [[10]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-cortexa9_mpcore):
  * **Multi-core support**. This is most evident by looking at Sony’s choice of a quad-core package.
    * As a side note, this also explains why portable devices like the iPad 2 and iPhone 4s (both carrying an A9) managed to debut a dual-core CPU.
  * **Out-Of-Order execution** through the use of [register renaming](https://www.copetti.org/writings/consoles/xbox-360/#revisiting-old-paradigms). This is a huge step for ARM in further scaling its [Instruction level parallelism](https://www.copetti.org/writings/consoles/xbox-360/#an-alternative-solution), considering other chips like PowerPC were forced to [abandon it](https://www.copetti.org/writings/consoles/xbox-360/#revisiting-old-paradigms).
    * This will also have a profound effect on the evolution of the ARM instruction set. You will see this in a future analysis of the Nintendo Switch.
  * A **variable-length pipeline** , between **8 and 11 stages** depending on the operation. The total number may also increase if execution continues in the multimedia co-processor (explained in the next section).


Moreover, Sony customised the package by adding one of ARM’s upgrades called **Primelink Level 2 Cache Controller** along with **2 MB of L2 cache** shared among all cores [[11]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-primelink_l2). Primelink is a flexible cache subsystem which can be programmed with different types of [cache associations](https://www.copetti.org/writings/consoles/xbox-360/#shared-cache), from direct mapping to 16-way. If you are curious, years later ARM renamed the Primelink brand to ‘CoreLink’ [[12]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-corelink_l2).
#### The grown-up ISA
The ARMv7 instruction set in the Cortex-A9 features a multitude of extensions. The majority of changes will be in the form of [SIMD capabilities](https://www.copetti.org/writings/consoles/dreamcast/#special-work) and multiprocessing, you’ll notice this when we take a closer look into the novelties of the ARMv7.
  * [A quick glance](https://www.copetti.org/writings/consoles/playstation-vita#tab-1-1-a-quick-glance)
  * [Overshadowing features](https://www.copetti.org/writings/consoles/playstation-vita#tab-1-2-overshadowing-features)


##### A quick glance
ARMv7 is a superset of the ARMv6 ISA. Its additions can be grouped into four areas: VFPv3, NEON, Security Extension and multi-processing. I explain each further down.
Moreover, the alternative [Thumb ISA](https://www.copetti.org/writings/consoles/game-boy-advance/#tab-2-3-squeezing-performance) (previously enhanced with [Thumb v2](https://www.copetti.org/writings/consoles/nintendo-ds/#tab-1-2-arm946e-s)) has undergone a major revision called **Thumb-2**. Truth to be told, it already debuted on embedded ARMv6 CPUs (implementing the ARMv6T2 variant), but it has now become a standard on the Cortex-A line.
On the other side, it’s worth mentioning that **ThumbEE** , the successor of the deprecated [Jazelle](https://www.copetti.org/writings/consoles/wii/#the-hidden-co-processor), has been left unused or even excluded from many Cortex-A CPUs. Surprisingly enough, Kermit’s Cortex-A9 CPU happens to implement ThumbEE and Jazelle [[13]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-main_processor), but I don’t think any application takes advantage of these. If you want an idea of its adoption back in the day, let me tell you that Dalvik (Android’s Java interpreter, to put it simply) didn’t even bother using Jazelle/Thumb-2EE at all. That tells you the general attitude towards ARM’s Java efforts.
« Previous [Next »](https://www.copetti.org/writings/consoles/playstation-vita#tab-1-2-overshadowing-features)
##### Overshadowing features
Back to the interesting bit, Thumb-2 is a significant revamp of Thumb because it **adds 32-bit instructions** [[14]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-thomas_thumb). Considering Thumb originally only bundled 16-bit opcodes, the new revision has now filled all the gaps when compared to the master ISA (ARM). Going forward, in contrast with ARM, Thumb-2 offers greater density and is only missing the [conditionals](https://www.copetti.org/writings/consoles/game-boy-advance/#commanding-the-cpu). Even so, Thumb-2 manages to bridge this functionality by including an exclusive `IT` instruction.
Nevertheless, Thumb’s renovation unfortunately means more fragmentation and confusion, eventually to the point assembler developers can’t decide which instruction set to use. _Lucky_ for them, ARM also devised a specification called **Unified Assembler Language** (UAL) that aimed to consolidate all ISAs into a single codebase that can target both ARM and Thumb-2 ISAs. This allows programs written in UAL to be assembled for all variants of Cortex CPUs (some of which implement ARM and Thumb-2 while others only support the latter). Behind the scenes, UAL is just the union of ARM and Thumb-2 opcodes, the assembler program then skips opcodes based on the target CPU. For instance, when it comes to writing a branching subroutine, programmers must write the two types of branching opcodes in the same routine (ARM’s conditionals and Thumb-2’s `IT` instruction) - effectively ‘duplicating’ code. However, the assembler then decides which opcodes to parse based on the target processor.
In the case of using programming languages (C, Objective-C, C++, etc.), the decision is much simpler, **compilers default to Thumb-2 for assembly generation** [[15]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-uni_fund), mainly due to its efficient code density and rare performance penalties. Thus, smartphone apps and, by extension, applications for the PSVita, are mainly compiled to Thumb-2 instead of ARM.
[« Previous](https://www.copetti.org/writings/consoles/playstation-vita#tab-1-1-a-quick-glance) Next »
##### More accelerators
The most notable component of the Cortex-A9, in particular for the PSVita, is the **Media Processing Engine** (MPE). This is ARM’s new coprocessor for 3D applications. It’s been engineered in a very convoluted way, however, as it executes two different but related instruction sets:
  * The **Vector Floating-Point v3** (VFPv3): A continuation of [VFPv2](https://www.copetti.org/writings/consoles/nintendo-3ds/#tab-1-1-the-original-mpcore) for floating-point capabilities. It’s IEEE-754 compliant and now extended to provide instructions like `VCVT` (to convert between fixed-point and floating-point values) and `VMOV` (to transfer values between the CPU and the FPU register file). This is helpful since **the VFP only understands 32-bit and 64-bit floating-point values**.
    * The exact variant included in the Cortex-A9 is called ‘VFPv3-D32’, meaning it includes **thirty-two 64-bit registers**.
    * Even though this ISA contains the word ‘vector’, ARMv7 deprecated the use of the vector instructions and the Cortex-A9 includes none [[16]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-cortexa9_mpe). _So much for being called a ‘vector FPU’…_
  * The **NEONv1** , also known as ‘ARMv7 Advanced SIMD’, is the _real_ vector instruction set, enabling to operate multiple scalars at once. NEON provides **sixteen 128-bit registers** , which can be also split into thirty-two 64-bit or 32-bit ‘virtual’ registers. The integers being operated may be as big as 64 bits, while floating-point types can’t surpass 32 bits.
    * It’s worth reminding that [Sony’s predecessor vector unit](https://www.copetti.org/writings/consoles/playstation-portable/#coprocessors) provided the immense amount of 128 registers, albeit 32-bit instead. If we do the math, the Cortex-A9 MPCore manages to match that number. Although, only 16 registers are accessible per core, and forget about the matrix-type addressing that made the VFPU special and efficient. On the bright side, perhaps there’s a new optimisation opportunity by having multiple cores compute SIMD instructions in parallel.


NEON and VFPv3 share the same register file, but they’re still considered separate ISAs. Considering ancestral processors like the SH-4 delivered SIMD operations [by simply extending its FPU](https://www.copetti.org/writings/consoles/dreamcast/#special-work), one can only wonder why ARM ended up producing two distinct ISAs. Well, the explanation is simple: **neither is feature-complete**. Particularly, **VFPv3 doesn’t support fixed-point** while **NEON is not compliant with the IEEE 754 standard** [[17]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-johnston). So, as an intermediate solution, the circuitry was segregated.
[![Image](https://www.copetti.org/images/consoles/psvita/axim.2a01779d1fb8a57e6be9e8da7700b6d1f53a6daced1f632cfcc592ad7ddda29a_hu_f41f3d738053725.png)](https://www.copetti.org/images/consoles/psvita/axim.2a01779d1fb8a57e6be9e8da7700b6d1f53a6daced1f632cfcc592ad7ddda29a.webp)The Dell Axim X51v (2005).  
This high-end PDA carried an Intel XScale PXA270 CPU, compatible with the ARMv5 ISA but also bundles proprietary SIMD extensions, which were only available on Intel’s CPU line. This conflicted with ARM’s business model. In response, ARM presented the NEONv1 set.  
By the way, this device also houses a PowerVR MBX GPU, which is related to the graphics chip of the PSVita.
All in all, this means the compiler will need to work harder optimising the code, but it still makes you wonder why ARM’s engineers ended up complicating things to absurd levels. In my opinion, I believe NEON was rushed to rapidly counter **Wireless MMX** (Intel’s proprietary SIMD extension for the XScale, released a year before) as ARM didn’t enjoy seeing Intel bundling exclusive instructions only available on the XScale [[18]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-mmx). This is also complemented by the fact the official documentation on Cortex’s timings was hurried as well [[19]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-timings).
### The master bus (or buses)
Another popular product from ARM, the [AMBA specification](https://www.copetti.org/writings/consoles/wii/#the-hidden-co-processor) designed for interconnecting components, carries forward with the Cortex-A9. Within its [third revision](https://www.copetti.org/writings/consoles/nintendo-3ds/#tab-1-3-the-axi-bus), the AXI protocol was selected for interfacing the cores within the MPCore cluster. Curiously enough, it’s the [same choice](https://www.copetti.org/writings/consoles/nintendo-3ds/#tab-1-3-the-axi-bus) found in the ARM11 and its well-known adopter, the Nintendo 3DS.
Speaking of which, remember Nintendo’s adoption of the **Open Core Protocol** (OCP) for [communicating with its PICA GPU](https://www.copetti.org/writings/consoles/nintendo-3ds/#adopting-open-standards)? Well, that’s also another protocol found in the PSVita, now used for all communications outside the MPCore [[20]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-memory_system).
### Envisioning the future
After the Cortex-A9, the line of succession became increasingly confusing. The Cortex-A series was broken down into **four more categories** , ranging from the top performer to the most energy-efficient. In doing so, the model numbering of each CPU became absurdly difficult to follow, but I guess it didn’t matter for the end user because these CPUs weren’t sold off-the-shelf!
The next big milestone for ARM will debut in 2011, with the arrival of ARMv8. I’ll talk more about this in a future article about the Nintendo Switch.
### The new media coprocessor
Next to the ARM cluster, Sony bundled a large accelerator meant to support gaming-related tasks. Just like the previous [Media Engine group](https://www.copetti.org/writings/consoles/playstation-portable/#multimedia-cpu), it is completely proprietary and acts as a black box. Programmers are not meant to fiddle with it directly but through the official SDK.
Having said that, this accelerator is called **Venezia**. This is a complete and separate CPU package designed by Sony’s close partner, Toshiba, for image and sound processing [[21]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-toshiba_press). With functionality closer to a Digital Signal Processor (DSP), Venezia was also sold as a [synthesisable chip](https://www.copetti.org/writings/consoles/game-boy-advance/#tab-1-2-a-new-cpu-venture) for multimedia appliances (i.e. DVD players) [[22]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-mep). Consequently, Sony selected it to accelerate multimedia tasks, so you could say it’s the spiritual successor of the [Media Engine](https://www.copetti.org/writings/consoles/playstation-portable/#multimedia-cpu).
  * [Architecture of Venezia](https://www.copetti.org/writings/consoles/playstation-vita#tab-2-1-architecture-of-venezia)
  * [A curious rendition](https://www.copetti.org/writings/consoles/playstation-vita#tab-2-2-a-curious-rendition)


#### Architecture of Venezia
[![Image](https://www.copetti.org/images/consoles/psvita/cpu/venezia.82c55d77c81ac06f3440dbc7b4c6d8a53d3bafdbef9ecec59ec607d79ba68c40.png)](https://www.copetti.org/images/consoles/psvita/cpu/venezia.82c55d77c81ac06f3440dbc7b4c6d8a53d3bafdbef9ecec59ec607d79ba68c40.png)Overview of Venezia.
Similarly to the MPCore, Venezia is a cluster, this time made of **eight ‘Media Processing Engine’ (MPE) cores** operating at **266.7 MHz**. Notice that its naming confusingly overlaps with ARM’s vector accelerators, but they are different silicon. That being said, each of Toshiba’s MPEs houses [[23]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-venezia):
  * A proprietary **‘Media-embedded Processor’ (MeP) CPU**. Particularly, a fifth revision called ‘MeP-c5’. This features a 32-bit RISC-based architecture.
  * **32 KB L1 cache** , split into 16 KB for instructions and 16 KB for data.
  * **64 KB** of general-purpose memory. This is where the MeP CPU executes its main program.
  * A **DMA controller** for transferring between internal and external memory.
  * An **‘Image Processing’ co-processor** named ‘IVC2’ that executes 64-bit SIMD instructions. It can operate different packs of data, from eight 8-bit integers to two 32-bit ones.
    * The IVC2 provides two 256-bit accumulator registers, which combined with other capabilities, it allows to compute two operations at the same time.


The cluster also features **256 KB of L2 cache** , but its main selling point is found in its instruction set, which is based on the **Very Long Instruction Word (VLIW) model**. Essentially, a single line can encode multiple instructions at once. In the case of Venezia, three instructions (two for the image coprocessor and one for the CPU) [[24]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-berkeley_dsp). This requires a very clever compiler capable of packing instructions efficiently, however.
« Previous [Next »](https://www.copetti.org/writings/consoles/playstation-vita#tab-2-2-a-curious-rendition)
#### A curious rendition
Interestingly enough, CPU designers once experimented with VLIW implementations back in the 90s when it was thought to be the future of mainstream CPUs. This led to Broadcom’s Firepath, the Transmeta Crusoe and, of course, the Intel Itanium - to name a few. However, the concept didn’t gain traction outside particular uses, as the resulting benchmarks proved disappointing. Thus, interests soon shifted to other parallelism techniques, such as [out-of-order execution](https://www.copetti.org/writings/consoles/playstation-2/#tab-1-1-outperforming-success), which transferred the burden back to the CPU.
Be as it may, Venezia is only accessible through an abstract API called ‘Codec Engine’ [[25]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-venezia), which implements different kinds of image and audio encoding/decoding tasks. For instance, there’s an **AVC decoding** command that decompresses video data encoded with ‘Advanced Video Coding’ (AVC) [[26]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-onscripter) and outputs an uncompressed stream the GPU understands.
[« Previous](https://www.copetti.org/writings/consoles/playstation-vita#tab-2-1-architecture-of-venezia) Next »
### Memory available
Enough about CPU talk! Let’s now take a look at the memory bundled within the PSVita.
As is customary with portable consoles, there are multiple memory types in this system.
#### Main memory
To start with, at the top of Kermit’s stack, we find a large block that houses **512 MB of LPDDR2 SDRAM** and is used as the main working area. In case you are now wondering “I get the ‘512 MB’ part, but what’s with all those initials?”, you’re not alone.
There’s a lot of terminology to unpack here, let’s start by breaking down the ‘LPDDR2 SDRAM’ name into two groups, from right to left, and then inspecting what’s inside each:
  1. **SDRAM** means ‘Synchronous Dynamic RAM’.
     * Dynamic RAM (DRAM) is the opposite of ‘Static RAM’ (SRAM). DRAM is cheaper to produce but exhibits more latency. That’s why CPU cache is made of SRAM while external general-purpose memory is made of DRAM.
     * Synchronous DRAM ([SDRAM](https://www.copetti.org/writings/consoles/xbox/#memory-layout)) means transfers are synchronised on par with the CPU clock, improving its throughput.
  2. **LPDDR2** means ‘Low Power Double Data Rate 2’.
     * Double Data Rate (DDR) states that transfers encode twice the information per cycle.
     * Low Power (LP) is a novelty here. This is not typical DDR, but a distinct variant called ‘Low Power’. It was initially conceived as a modification of DDR SDRAM, then became its own brand alongside others (as it happened with [GDDR](https://www.copetti.org/writings/consoles/wiiu/#gddr3-or-ddr3)). While DDR evolves to increase the bandwidth, new revisions of LP focus on reducing its operating voltage. As you may guess, its main adopters are phones and laptops.
     * The ‘2’ at the end signifies it’s the second revision of LPDDR. Its specification was published in 2009 and, among other improvements, it only needs 1.2 Volts to work (compared to 1.35 V for DDR3).


#### Other memory
There’s another large block of **128 MB of Custom DRAM (CDRAM)** predominantly connected to the GPU. ‘CDRAM’ is just an internal name to denote traditional SDR SDRAM which, unlike Double Data Rate (DDR) memory, this one is Single Data Rate. Although, being a dedicated space close to the GPU makes it ideal for intensive graphics operations, which may explain why this block is apparently connected using **two 512-bit buses** [[27]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-chip_james).
Apart from that, the SoC also fits an extra **~2.18 MB of SRAM** split into different blocks [[28]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-memory):
  * 2 MB named ‘Camera SRAM’.
  * 32 KB named ‘SPAD32K’.
  * 128 KB named ‘SPAD128K’.
  * 4 KB named ‘SceCompatSharedSram’.
  * 16 KB named ‘Scratchpad’.


On the other hand, they are all reserved for the operating system, but we’ll discuss them in a later section. By the way, you may want to know that those 16 KB of ‘Scratchpad’ coincide with amount of SRAM also found in the [PlayStation Portable](https://www.copetti.org/writings/consoles/playstation-portable/#memory-available), you’ll soon see why.
### One last CPU
Last but not least, there’s an additional CPU inside Kermit: The old **[MIPS32 4k](https://www.copetti.org/writings/consoles/playstation-portable/#the-new-portable-cpu)** (the same one bundled with the [PlayStation Portable](https://www.copetti.org/writings/consoles/playstation-portable/)) [[29]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-trinity). The intention was to provide backwards compatibility with [PlayStation Portable](https://www.copetti.org/writings/consoles/playstation-portable/) and [PlayStation 1](https://www.copetti.org/writings/consoles/playstation/) games. That’s the one and only (official) use for the MIPS CPU, with no co-processing capability in place.
[![Image](https://www.copetti.org/images/consoles/psp/tachyon.a7c25cb952548e37638dbaf3bf0dc7719c4e7824426d34c915caa5c5115a2677.jpg)](https://www.copetti.org/images/consoles/psp/tachyon.a7c25cb952548e37638dbaf3bf0dc7719c4e7824426d34c915caa5c5115a2677.jpg)The predecessor ‘Tachyon’ chip found on the PSP, housing the MIPS CPU and many other components.
Speaking of backwards compatibility, Kermit doesn’t include the [Media Engine](https://www.copetti.org/writings/consoles/playstation-portable/#multimedia-cpu) [[30]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-robots), although being a black box means that the software doesn’t care about what’s behind the scenes. Thus, the functions of that co-CPU are replicated through Venezia instead.
For the remaining I/O, MIPS is not physically connected to the rest of the hardware, only the Cortex-A9 is. Thus, the PSP emulation software (running on the MIPS CPU) requests services to the ARM CPU by following the ‘Remote Procedure Call’ (RPC) model [[31]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-trinity) [[32]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-davee_kermit).
Finally, 64 MB of CDRAM are also reserved for this service. Those 16 KB of ‘Scratchpad’ I mentioned before are actually housed within the MIPS CPU [[33]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-gh_feedback), and are subsequently allocated to the PSP emulator [[34]](https://www.copetti.org/writings/consoles/playstation-vita#bib:cpu-memory), as original PSP games [would expect to find](https://www.copetti.org/writings/consoles/playstation-portable/#memory-available).
* * *
## Next: Graphics
That’s it for now! In the next part we’ll take a look at [VideoLogic](https://www.copetti.org/writings/consoles/dreamcast/#graphics)’s evolution to become a leading GPU in the mobile market, culminating in their signature PowerVR MBX GPU. [Stay tuned](https://www.copetti.org/writings/consoles/#stay-updated) for the next delivery!
* * *
## Contributing
This article is part of the [Architecture of Consoles](https://www.copetti.org/writings/consoles/) series. If you found it interesting then please consider donating. Your contribution will be used to fund the purchase of tools and resources that will help me to improve the quality of existing articles and upcoming ones.
[![Donate with PayPal](https://www.copetti.org/images/paypal_donate.png)](https://www.paypal.com/donate/?hosted_button_id=3GXQA6XPL7G3S)
[![Become a Patreon](https://www.copetti.org/images/patreon.png)](https://www.patreon.com/copetti)
You can also buy the [book editions](https://www.copetti.org/writings/consoles/materials/book/) in English. I treat profits as donations.
[![eBook edition](https://www.copetti.org/images/consoles/books/ebooks_banner.0d180c0136e4c9345bc0ab4f7a0224849a292326d2679d610ea945054383a996.jpg)](https://www.copetti.org/writings/consoles/materials/book/)
Big thanks to the following people for their donation:
```
- All of the generous eBook readers
- Adam Obenauf
- Adrian Burgess
- Alberto Massidda
- Alex Christensen
- Andrei Zbikowski
- Andrew Woods
- Angus MacMullen
- Antonio Bellotta
- Ben Morris
- Bitmap Bureau
- CLEMENT frederic
- Colin Weltin-Wu
- CyberpunkDre
- D
- Daniel Cassidy
- Dillon A
- Elizabeth Isley
- Grady Haynes
- Hadlee Simons
- James William Jones
- jmi2k
- João Baptista
- ltlollo
- Luke Groeninger
- Luke Wren
- Marc C.
- Marek Vybiral
- MCE
- Mia
- Nicholas T.
- Owen Christensen
- Paul Gerver
- Pedro Henrique Martins Garcia
- petey893
- Red Wolf
- Rodrigo Groppa
- Sanqui
- Sara Sinback
- Sariya Melody
- Scott Munro
- Stephane Dallongeville
- Str33tz
- TadeusTaD
- Thomas Finch
- Thomas Peter Berntsen
- Tobias Gruetzmacher
- Tomas Arriagada
- znix
```

Alternatively, you can help out by [suggesting changes](https://github.com/flipacholas/Architecture-of-consoles) and/or [adding translations](https://github.com/flipacholas/Architecture-of-consoles).
* * *
## Copyright and permissions
This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). You may use it for your work at no cost, even for commercial purposes. But you have to respect the license and reference the article properly. Please take a look at the following guidelines and permissions:
Article information and referencing
For any referencing style, you can use the following information:
  * **Title of article** : PlayStation Vita Architecture (Part 1) - A Practical Analysis
  * **Author** : Rodrigo Copetti
  * **URL** : <https://www.copetti.org/writings/consoles/playstation-vita/>
  * **Date of publication** : October 23, 2024
  * **Last modified** : April 18, 2025


For instance, to use with BibTeX:
```
@misc{copetti-psvita,
    url = {https://www.copetti.org/writings/consoles/playstation-vita/},
    title = {PlayStation Vita Architecture (Part 1) - A Practical Analysis},
    author = {Rodrigo Copetti},
    year = {2024}
}

```

or a IEEE style citation:
```
[1]R. Copetti, "PlayStation Vita Architecture (Part 1) - A Practical Analysis", Copetti.org, 2024. [Online]. Available: https://www.copetti.org/writings/consoles/playstation-vita/. [Accessed: day- month- year].

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
### CPU
  * Vita Development Wiki contributors, [Kermit](https://wiki.henkaku.xyz/index.php?title=Kermit&oldid=21314) (accessed 08-August-2024). Vita Development Wiki. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:1)
  * Toshiba, [Semiconductor & storage products company](https://web.archive.org/web/20120713080459/http://www.toshiba-components.com/ASIC/SiP.html). Archived. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:2)
  * ARM Limited, Cortex-A8 MPCore - technical reference manual. 2010. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:6)
  * ARM Limited, Architecture and implementation of the ARM cortex-A8 microprocessor - white paper. 2005. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:7)
  * Phillip Johnston, Demystifying ARM floating point compiler options. 2017. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:17)
  * ARM Limited, ARM cortex-A9 MPCore - technical reference manual. 2016. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:10)
  * ARM Limited, Cortex-A9 NEON media processing engine - technical reference manual. 2012. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:16)
  * Mark Lapedus, Peter Clarke, [Intel distances itself from ARM with wireless MMX](https://www.eetimes.com/intel-distances-itself-from-arm-with-wireless-mmx/). 2002. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:18)
  * Ben Avison, [ARM cortex-A8 instruction timings](http://www.avison.me.uk/ben/programming/cortex-a8.html). 2010. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:19)
  * ARM Limited, PrimeCell level 2 cache controller (PL310) - technical reference manual. 2008. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:11)
  * ARM Limited, CoreLink level 2 cache controller L2C-310 - technical reference manual. 2012. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:12)
  * YuriSizuku, [ONScripter-jh-PSVita (yuri)](https://github.com/YuriSizuku/psv-OnscripterJH/blob/master/README.md). Github. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:26)
  * Andy Nguyen, [Trinity: PSP emulator escape](https://theofficialflow.github.io/2019/06/18/trinity.html). TheFloW's security blog. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:31)
  * Vita Development Wiki contributors, [Venezia](https://wiki.henkaku.xyz/vita/Venezia) (accessed 08-September-2024). Vita Development Wiki. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:25)
  * Davee, [Kermit](https://www.lolhax.org/2012/03/29/kermit/). [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:32)
  * robots, [Native resolution for PSP games on PSVITA.](https://github.com/vita-nuova/bounties/issues/5#issuecomment-520315925). Github. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:30)
  * Vita Development Wiki contributors, [Physical memory](https://wiki.henkaku.xyz/vita/Physical_Memory) (accessed 11-September-2024). Vita Development Wiki. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:34)
  * Toshiba, [Toshiba launches image recognition processors for automotive applications](https://www.global.toshiba/ww/news/corporate/2011/10/pr1301.html). 2011. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:21)
  * Berkeley Design Technology, Inc., [BDTI releases benchmark results for toshiba’s venezia platform](https://www.bdti.com/InsideDSP/2009/04/22/Bdti). 2009. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:24)
  * Toshiba, [Media embedded processor - what is MeP](https://web.archive.org/web/20060523085417/http://www.mepcore.com/english/frameset1_e.html). Archived. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:22)
  * Arm, [The ARM university program, ARM architecture fundamentals](https://www.youtube.com/watch?v=7LqPJGnBPMM) (accessed 18-October-2024). [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:15)
  * David Thomas, [ARM > introduction to ARM > thumb-2](https://www.davespace.co.uk/arm/introduction-to-arm/thumb-2.html). 2012. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:14)
  * David Thomas, [ARM > introduction to ARM > architecture 7](https://www.davespace.co.uk/arm/introduction-to-arm/arm-arch7.html). 2012. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:3)
  * Wiki Contributors, [Samsung galaxy s III (samsung-m0) - postmarketOS wiki](https://wiki.postmarketos.org/wiki/Samsung_Galaxy_S_III_%28samsung-m0%29) (accessed 22-October-2024). [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:5)
  * Vita Developer Contributors, [CPU - vita developer wiki](https://www.psdevwiki.com/vita/CPU) (accessed 22-October-2024). [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:4)
  * Vita Development Wiki contributors, [DMAC](https://wiki.henkaku.xyz/vita/DMAC) (accessed 08-November-2024). Vita Development Wiki.
  * Vita Development Wiki contributors, [Main processor](https://wiki.henkaku.xyz/vita/Main_Processor) (accessed 08-November-2024). Vita Development Wiki. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:13)
  * Vita Development Wiki contributors, [Memory system](https://wiki.henkaku.xyz/vita/Memory_System) (accessed 08-November-2024). Vita Development Wiki. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:20)
  * ARM Limited, Cortex-M3 devices - generic user guide. 2010. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:8)
  * CreepNT, [PlayStation vita: Various comments](https://github.com/flipacholas/Architecture-of-consoles/issues/354) (accessed 10-November-2024). Github. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:33)
  * Dick James, [Sony’s PS vita uses chip-on-chip SiP - 3D, but not 3D](https://web.archive.org/web/20150425204407/http://www.chipworks.com/en/technical-competitive-analysis/resources/blog/sonys-ps-vita-uses-chip-on-chip-sip-3d-but-not-3d/) (Archived - accessed 11-November-2024). Chipworks. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:27)
  * ARM Limited, ARM cortex-a series programmer’s guide. 2013. [↩︎](https://www.copetti.org/writings/consoles/playstation-vita#bibref:9)


### Photography
  * Evan Amos, [The vanamo online game museum](https://commons.wikimedia.org/wiki/User:Evan-Amos).
  * Rodrigo Copetti (Me), [Diagrams, casual photos, screenshots and videos](https://www.copetti.org/).


* * *
## Changelog
It’s always nice to keep a record of changes. For a complete report, you can check the [commit log](https://github.com/flipacholas/Architecture-of-consoles/commits/master/articles/playstation-vita.Rmd.md). Alternatively, here’s a simplified list:
```
### 2024-11-10
- Round of corrections. See https://github.com/flipacholas/Architecture-of-consoles/issues/354 (thanks @CreepNT and @bythos14).
### 2024-10-23
- First part published!
### 2024-10-22
- Feedback corrections. Thanks @dpt, @jaylon, @subayashi05 and @incognitojam.
### 2024-10-20
- First Part 1 draft finished.
- Made in 🇬🇧 UK, 🇳🇱 Netherlands, 🇪🇸 Spain and 🇺🇸 USA.
```

* * *
[« Nintendo 3DS Architecture](https://www.copetti.org/writings/consoles/nintendo-3ds/) [Wii U Architecture »](https://www.copetti.org/writings/consoles/wiiu/)
![Rodrigo Copetti](https://www.copetti.org/favicon/favicon.png)
### Rodrigo Copetti
I hope you have enjoyed this article! If you want to know more about the author [tap here](https://www.copetti.org/about/) and if you would like to support him [tap here](https://www.copetti.org/support/) instead
[Tweet ](https://twitter.com/intent/tweet?text=PlayStation%20Vita%20Architecture%20%28Part%201%29%20%7c%20A%20Practical%20Analysis%20https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fplaystation-vita%2f)[Share ](javascript:void\(0\))[Share ](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fplaystation-vita%2f&title=PlayStation%20Vita%20Architecture%20%28Part%201%29%20%7c%20A%20Practical%20Analysis&summary=An%20in-depth%20analysis%20that%20explains%20how%20this%20console%20works%20internally&source=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fplaystation-vita%2f)[Share](https://reddit.com/submit?url=https%3a%2f%2fwww.copetti.org%2fwritings%2fconsoles%2fplaystation-vita%2f&title=PlayStation%20Vita%20Architecture%20%28Part%201%29%20%7c%20A%20Practical%20Analysis)
[Switch to classic edition](https://classic.copetti.org/writings/consoles/playstation-vita/)
Rodrigo Copetti © 2025 [](https://www.copetti.org/index.xml)
[About the website and its content](https://www.copetti.org/disclaimer/)
rsslinkedintwitterblueskygithub facebookreddit
