# Benchmark sets for free energy calculations

This repository relates to the *[perpetual review](https://arxiv.org/abs/1502.01329)* paper called "[Predicting binding free energies: Frontiers and benchmarks](http://biorxiv.org/content/early/2016/09/11/074625)" by David L. Mobley and Michael Gilson. Its focus is benchmark sets for binding free energy calculations, including the perpetual review paper, but also all things relating to benchmark sets for free energy calculations. This includes discussion, datasets, and standards for datasets and data deposition.

All versions -- current and prior -- are available via Zenodo DOIs, with the latest version at this DOI: [![DOI](https://zenodo.org/badge/67898475.svg)](https://zenodo.org/badge/latestdoi/67898475)


## The paper

The paper was just submitted (Sept. 10, 2016) to [bioRxiv](http://biorxiv.org/content/early/2016/09/11/074625) and Annual Reviews in Biophysics. Its source files are deposited here, as detailed below, and comments/suggestions, etc. are welcome via the issue tracker (https://github.com/MobleyLab/benchmarksets/issues).

The paper's authors are David L. Mobley (UC Irvine) and Michael K. Gilson (UCSD).

## The vision

The field vitally needs benchmark sets to test and advance free energy calculations, as we detail in our paper. 
Currently, there are no such standard benchmark systems.
And when good test systems are found, the relevant data tends to be published but then forgotten, and never becomes widely available. 
Here, we want the community to be involved in selecting benchmark systems, highlighting their key challenges, and making the data and results readily available to drive new science.

To make this happen, we need community input. 
Please bring new, relevant work to our attention, including experimental or modeling work on the benchmark systems currently available here, or new work on systems that might make good candidate benchmark systems for the future. 
And please help us create consensus around a modest set of benchmark systems which can be used to drive forward progress in the field.


## The benchmark sets

Currently proposed benchmark sets are detailed in [the paper](https://github.com/MobleyLab/benchmarksets/blob/master/paper/benchmarkset.pdf "Benchmark Sets") and include:
* Host guest systems
    * CB7
    * Gibb deep cavity cavitands (GDCCs) OA and TEMOA
* Lysozyme model binding sites
    * apolar L99A
    * polar L99A/M102Q

Other near-term candidates include:
* Thrombin
* Bromodomains
* Suggest and vote on your favorites via a feature request below

Community involvement is needed to pick and advance the best benchmarks.

## Get involved

We need your help to pick the most informative systems, identify the challenges they present, and help make them standard benchmarks. Please provide your input:

### Vote on what we should do next

For long-term directions, please help us prioritize what we ought to be doing in terms of benchmarks and other changes. Please click below to vote on one of these priorities or to suggest your own (such as addition of specific benchmark systems):

[![Feature Requests](http://feathub.com/MobleyLab/benchmarksets?format=svg)](http://feathub.com/MobleyLab/benchmarksets)

### Submit an issue

If you have a specific suggestion or request relating to the material on GitHub or our paper, please submit a request on our [issue tracker](https://github.com/MobleyLab/benchmarksets/issues).

### Submit a pull request

We also welcome contributions to the material which is already here to extend it (see Section IV in our paper) and encourage you to actually propose changes via a "pull request", even to the paper itself. This will allow us to track your contributions, as well. Specifically, the full list of contributors to the updated paper and data can be appended to subsequent versions of this work, as they would be for a software project.

## Contributors
- David Slochower (UCSD, Gilson lab): Grammar corrections and improved table formatting
- Nascimento (in a comment on biorxiv): Highlighted PDB code error for n-phenylglycinonitrile
- Jian Yin (UCSD, Gilson lab): Provided host-guest structures and input files for the host-guest sets described in the paper

## Versions
- [v1.0](https://github.com/MobleyLab/benchmarksets/releases/tag/v1.0): As posted to bioRxiv 
- v1.0.1 ([10.5281/zenodo.155330](https://doi.org/10.5281/zenodo.15533)): Incorporating improved tables and typo fixes from D. Slochower; also, versions now have unique DOIs via Zenodo.
- v1.0.4 ([10.5281/zenodo.167349](http://doi.org/10.5281/zenodo.167349)): Maintenance version fixing an incorrect PDB code and adding a new reference and some new links.
- v1.1 ([10.5281/zenodo.197428](http://doi.org/10.5281/zenodo.197428)): Adds significant additional discussion on potential future benchmark sets, needs for workflow science, etc. See release notes for more details. Versions also now include the date and version number within the PDF.

## Changes not yet in a release
- Added host-guest structures and input files on 12/19/16 (see [PR 22](https://github.com/MobleyLab/benchmarksets/pull/22)).

## Manifest

* paper: Provides LaTeX source files for the manuscript as submitted to bioRxiv (reformatted from the version submitted to Ann. Rev. and with 2D structures added to the tables); images, etc. are also available in sub-directories, as is the supporting information.
* input_files: Host-guest structures and simulation input files for the host-guest benchmark sets proposed in the paper (provided by Jian Yin from the Gilson lab)
