import json
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field
from pydantic.json_schema import GenerateJsonSchema


class BaseModelWrap(BaseModel):
    model_config = ConfigDict(validate_assignment=True, extra="forbid")


class Reference(BaseModelWrap):
    url: Optional[str] = Field(default=None, description="A web link")
    first_name: Optional[str] = Field(
        default=None, description="Author's first name"
    )
    last_name: Optional[str] = Field(
        default=None, description="Author's last name"
    )
    title: Optional[str] = Field(
        default=None, description="Title of the reference"
    )
    pages: Optional[str] = Field(default=None, description="Page numbers")
    year: Optional[str] = Field(default=None, description="Year of publication")
    date: Optional[str] = Field(default=None, description="Date of publication")
    journal: Optional[str] = Field(default=None, description="Name of journal")
    chapter: Optional[str] = Field(default=None, description="Chapter name")
    place: Optional[str] = Field(
        default=None, description="Place of publication"
    )
    editor: Optional[str] = Field(default=None, description="Editor")


class Example(BaseModelWrap):
    text: str = Field(description="Example usage sentence")
    translation: Optional[str] = Field(
        default=None, description="Spanish translation of the example sentence"
    )
    ref: Optional["Reference"] = Field(default=None, description="")


class Sense(BaseModelWrap):
    glosses: list[str] = Field(
        description="list of gloss strings for the word sense (usually only one). This has been cleaned, and should be straightforward text with no tagging."
    )
    tags: list[str] = Field(
        default=[],
        description="list of gloss strings for the word sense (usually only one). This has been cleaned, and should be straightforward text with no tagging.",
    )
    categories: list[str] = Field(
        default=[],
        description="list of sense-disambiguated category names extracted from (a subset) of the Category links on the page",
    )
    examples: list["Example"] = Field(
        default=[], description="List of examples"
    )
    subsenses: list["Sense"] = Field(
        default=[], description="List of subsenses"
    )
    senseid: Optional[int] = Field(
        default=None, description="Sense number used in Wiktionary"
    )


class Spelling(BaseModelWrap):
    alternative: Optional[str] = Field(
        default=None, description="Alternative spelling with same pronunciation"
    )
    note: Optional[str] = Field(
        default=None, description="Note regarding alternative spelling"
    )
    same_pronunciation: Optional[bool] = Field(
        default=None,
        description="Whether the alternative spelling has the same pronunciation as the default spelling",
    )


class Sound(BaseModelWrap):
    ipa: list[str] = Field(
        default=[], description="International Phonetic Alphabet"
    )
    phonetic_transcription: list[str] = Field(
        default=[], description="Phonetic transcription, less exact than IPA."
    )
    audio: list[str] = Field(default=[], description="Audio file name")
    wav_url: list[str] = Field(default=[])
    ogg_url: list[str] = Field(default=[])
    mp3_url: list[str] = Field(default=[])
    flac_url: list[str] = Field(default=[])
    roman: list[str] = Field(
        default=[], description="Translitaration to Roman characters"
    )
    syllabic: list[str] = Field(
        default=[], description="Syllabic transcription"
    )
    tag: list[str] = Field(
        default=[], description="Specifying the variant of the pronunciation"
    )


class WordEntry(BaseModelWrap):
    """WordEntry is a dictionary containing lexical information of a single word extracted from Wiktionary with wiktextract."""

    word: str = Field(description="word string")
    pos: str = Field(default=None, description="Part of speech type")
    pos_title: str = Field(default=None, description="Original POS title")
    lang_code: str = Field(
        description="Wiktionary language code", examples=["es"]
    )
    lang_name: str = Field(
        description="Localized language name of the word", examples=["español"]
    )
    senses: Optional[list[Sense]] = []
    categories: list[str] = Field(
        default=[],
        description="list of non-disambiguated categories for the word",
    )
    sounds: Optional[list[Sound]] = []
    spellings: Optional[list[Spelling]] = []


if __name__ == "__main__":

    class JsonSchemaGenerator(GenerateJsonSchema):
        def generate(self, schema, mode="validation"):
            json_schema = super().generate(schema, mode=mode)
            json_schema["title"] = "Spanish Wiktionary"
            json_schema["$id"] = "https://kaikki.org/es.json"
            json_schema["$schema"] = self.schema_dialect
            return json_schema

    with open("json_schema/es.json", "w") as f:
        json.dump(
            WordEntry.model_json_schema(schema_generator=JsonSchemaGenerator),
            f,
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )
