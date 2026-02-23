import os
import sys

# Suppress FutureWarning messages
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

# Disable progress bar during inference
# (tqdm used by fish_speech.models.text2semantic.inference.decode_n_tokens)
os.environ["TQDM_DISABLE"] = "1"

import datasets
import streamlit as st

# Trick to import local packages when this script is run from the terminal
sys.path.append(os.path.abspath("."))

from config import TTS_MODELS


st.set_page_config(
    page_title="TTS Common-Voice Demo", page_icon=None,
    layout="wide", initial_sidebar_state="auto",
    menu_items=None)


# Corpus and TTS model selection
# with st.sidebar:
#     corpus_name = st.selectbox(
#         "corpus_name",
#         key="corpus_name",
#         options=CORPUS_LIST,
#         index=get_index_from_query("corpus_name", CORPUS_LIST))
#     tts_name = st.selectbox(
#         "TTS",
#         key="tts_name",
#         options=TTS_MODELS,
#         index=get_index_from_query("tts_name", TTS_MODELS))
#     force_reload = st.button("Force reload")


################################################################################
# Main page                                                                    #
################################################################################

corpus = "blurb-biosses"
sample_id = "20"
sample_filename = "20_s1.0.wav"
sample_ref = """\
Recently, miR-126 was identified as a metastasis suppressing miRNA that is \
downregulated in relapsing breast cancer, leukemia, and cervical cancer."""

cv_dataset_path: str = "voice_samples/common_1k"  # Path to a set of voices
cv_ids = [
    "18099400",
    "18840889",
    "15734171",
    "18843978",
]

voices_ds = datasets.load_dataset(cv_dataset_path, split="train")
voices_ds = [
    voices_ds.filter(lambda s: str(s['voice_id']) == _id)[0]
    for _id in cv_ids
]


st.title("TTS Common-Voice Demo")

st.header(corpus)
st.markdown(f"**Sample:** {sample_id} | {sample_filename}")
st.text(f'"{sample_ref}"')

st.divider()

for voice in voices_ds:
    st.markdown(f"**{voice['voice_id']} {voice['gender'].capitalize()} {voice['accent'].capitalize()}**")

    col1, col2 = st.columns([0.2, 0.8], width=600)
    col1.text("Ref:")
    col2.audio(f"data/cv_clips/{voice['path'].replace('.mp3', '.wav')}")

    for tts in TTS_MODELS:
        col1, col2 = st.columns([0.2, 0.8], width=600)
        col1.text(f"{tts}:")
        col2.audio(f"data/tts/{tts}/{corpus}-cv/{voice['voice_id']}/{sample_filename}")

    st.space("small")


st.divider()

st.markdown(f"**Kokoro voice: Isabella Female British**")

col1, col2 = st.columns([0.2, 0.8], width=600)
col1.text("Kokoro:")
col2.audio(f"data/tts/kokoro/{corpus}/{sample_filename}")

for tts in TTS_MODELS:
    col1, col2 = st.columns([0.2, 0.8], width=600)
    col1.text(f"{tts}:")
    col2.audio(f"data/tts/{tts}/{corpus}/{sample_filename}")
