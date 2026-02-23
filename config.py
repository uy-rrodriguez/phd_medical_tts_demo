# DATASETS_DEFAULT = "train"
CORPUS_BLURB = {
    "ner": {
        "blurb-bc2gm":          "data/blurb/ner/BC2GM_hf",
        "blurb-bc5cdr-chem":    "data/blurb/ner/BC5CDR-chem_hf",
        "blurb-bc5cdr-disease": "data/blurb/ner/BC5CDR-disease_hf",
        "blurb-jnlpba":         "data/blurb/ner/JNLPBA_hf",
        "blurb-ncbi-disease":   "data/blurb/ner/NCBI-disease_hf",
    },
    "rel": {
        "blurb-chemprot":       "data/blurb/rel/chemprot_hf",
        "blurb-ddi":            "data/blurb/rel/DDI_hf",
        "blurb-gad":            "data/blurb/rel/GAD_hf",
    },
    "doc": {
        "blurb-hoc":            "data/blurb/doc/HoC_hf",
    },
    "sim": {
        "blurb-biosses":        "data/blurb/sim/BIOSSES_hf",
    },
    "qa": {
        "blurb-bioasq":         "data/blurb/qa/bioasq_hf",
        "blurb-pubmedqa":      "data/blurb/qa/pubmedqa_hf",
    },
}
CORPUS_LIST = sorted([k for v in CORPUS_BLURB.values() for k in v])

TTS_MODELS = [
    "fish-speech",
    "style-tts2",
    "zipvoice",
]
