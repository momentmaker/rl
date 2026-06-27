🌐 last30days v3.3.2 · synced 2026-06-27

What I learned:

**The fUS conversation right now is being driven by Aleph Neuro's "stunning brain images" launch, not by academic radiology** - The single loudest signal in the window is [@alephneuro](https://x.com/alephneuro)'s launch thread (489 likes), framing non-invasive neural decoding as "newly tractable" and arguing that ultrasound can "in theory achieve the specs needed for decoding the brain: mm-resolution and wide brain coverage, accomplishing what fMRI can do as a device that fits in the palm of your hand." [Businesswire](https://www.businesswire.com/news/home/20260625817511/en/Butterfly-Networks-Embedded-Partner-Aleph-Neuro-Unveils-Stunning-Brain-Images) confirms the substance: built on Butterfly Network's ultrasound-on-chip, Aleph claims the highest-resolution noninvasive 3D images of the human brain ever taken from outside the skull, using FDA-approved microbubbles to beat the usual diffraction limit.

**Where fUS clearly beats fMRI, per practitioners, is sensitivity, speed, portability and bedside access** - The recurring researcher claim is temporal and spatial: fUS routinely hits ~100 um in-plane resolution and ~400 ms sampling, while fMRI's BOLD signal has an intrinsic ~10-second hemodynamic lag that caps effective sampling near 0.1 Hz, per [MIT Press Imaging Neuroscience](https://direct.mit.edu/imag/article/doi/10.1162/imag_a_00030/117893/High-sensitivity-mapping-of-brain-wide-functional). Clinicians value that it is mobile and combinable with EEG or optogenetics, and that it can image populations who can't tolerate an MRI scanner - neonates and patients on the operating table. The strongest clinical proof point is intra-operative: [Frontiers in Neuroscience](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2019.01384/full) reports fUS during awake brain surgery mapping deep functional areas for language tasks at 300 um / 1.5-2.0 ms and distinguishing tumor from healthy vasculature in real time, something pre-operative fMRI cannot do.

**Where it falls short is the skull, the read-vs-write gap, and the same slow hemodynamic ceiling fMRI has** - The honest counterweight comes from researchers themselves. [@Goro_s_work](https://x.com/Goro_s_work/status/2070714607459782880) put the tradeoff cleanly: "functional ultrasound reads blood flow, so it's spatially rich but slow vs electrodes. The open bet is whether read-depth can beat invasive bandwidth." And because fUS measures cerebral blood volume, it inherits neurovascular coupling's lag - it is faster than fMRI but still indirect, not a true electrical readout. The bigger limiter is the skull: [Scientific Reports / PMC](https://www.nature.com/articles/s41598-024-81243-y) notes the skull is highly absorbing at imaging frequencies, leaving the cerebellum, auditory cortex, temporal and insular regions hard to image, and fully transcranial volumetric fUS during stimulation has not yet been demonstrated. Skeptics on X echo the "show me" mood, with [@HiSohan](https://x.com/HiSohan/status/2070588650023424112) noting people "compare with fMRI without detailing how ultrasound can capture functional data."

**The framing shifting hardest in 2026 is fUS-as-BCI, not fUS-as-scanner** - [@SumnerLN](https://x.com/SumnerLN/status/2070579719855395147) of Forest Neurotech (18 likes) credits the hardware leap: "Aleph built on the ultrasound-on-chip from @ButterflyNetInc - the same chip we used for sub-mm functional brain imaging at @ForestNeurotech. One coin-sized chip, capable of whole heart ULM, whole brain functional imaging, and even whole body imaging." [Forest Neurotech](https://forestneurotech.org/) is shipping Forest 1, a key-fob-sized scanner for imaging and neuromodulation, and [Caltech](https://www.caltech.edu/about/news/ultrasound-enables-less-invasive-brainmachine-interfaces) has demonstrated closed-loop online fUS-BMI decoding movement intentions without implants - positioning fUS as the less-invasive middle ground between scalp EEG and Neuralink-style electrode arrays, per [IEEE Spectrum](https://spectrum.ieee.org/bci-ultrasound).

KEY PATTERNS from the research:
1. The loudest fUS news this month is commercial, not clinical - Aleph Neuro's noninvasive 3D imaging launch on Butterfly's ultrasound-on-chip, per [@alephneuro](https://x.com/alephneuro/status/2070183640143982907)
2. Practitioners pitch fUS as beating fMRI on sensitivity, speed (~100 um / ~400 ms vs ~0.1 Hz BOLD), portability, and access to infants and OR patients, per [MIT Press](https://direct.mit.edu/imag/article/doi/10.1162/imag_a_00030/117893/High-sensitivity-mapping-of-brain-wide-functional)
3. The headline limitation researchers admit is the skull - cerebellum, temporal, auditory and insular regions stay hard, and full transcranial volumetric fUS isn't proven yet, per [Scientific Reports](https://www.nature.com/articles/s41598-024-81243-y)
4. The read/write debate is live: fUS is "spatially rich but slow vs electrodes," so the open question is whether non-invasive read-depth can rival invasive bandwidth, per [@Goro_s_work](https://x.com/Goro_s_work/status/2070714607459782880)
5. fMRI is not standing still - the same window saw researchers celebrating resting-state fMRI's proven clinical translation, a reminder fUS is racing a maturing incumbent, per [@bttyeo](https://x.com/bttyeo/status/2070691294192799975)

---
✅ All agents reported back!
├─ 🟠 Reddit: 15 threads │ 2,337 upvotes │ 990 comments
├─ 🔵 X: 12 posts │ 49 likes │ 4 reposts
├─ 🌐 Web: 8 pages - frontiersin.org, direct.mit.edu, sciencedaily.com, radiologyinfo.org, sciencedirect.com, fusfoundation.org, ajnr.org
├─ 🗣️ Top voices: @SumnerLN, @Goro_s_work, @HiSohan │ r/artificial, r/cogsci, r/BCI
└─ 📎 Raw results saved to /private/tmp/rl_raw_20260627/functional-ultrasound-fus-brain-imaging-raw-v3b.md
---

I'm now an expert on functional ultrasound (fUS) brain imaging. Some things I can help with:
- Break down the Aleph Neuro vs Forest Neurotech approaches and whether ultrasound-on-chip really makes fUS a consumer-scale BCI
- Go deeper on exactly where fUS beats vs loses to fMRI for a specific use case (neonatal imaging, intra-operative mapping, or neural decoding)
- Explain the skull-penetration problem and how microbubbles plus deep-learning reconstruction are being used to get around it

I have all the links to the 15 Reddit threads, 12 X posts, and 8 web pages I pulled from. Just ask.
