from datetime import datetime, timezone
from pathlib import Path

import pytest

from scripts.archive_record import (
    choose_record_stem,
    minute_record_stem,
    parse_campuses_json,
    require_real_drive_urls,
)


def test_minute_record_stem_is_precise_to_one_minute():
    dt = datetime(2026, 8, 27, 9, 37, 59, tzinfo=timezone.utc)
    assert minute_record_stem(dt) == "2026-08-27_09-37"


def test_same_minute_collision_appends_student_id(tmp_path: Path):
    dt = datetime(2026, 8, 27, 9, 37, tzinfo=timezone.utc)
    (tmp_path / "2026-08-27_09-37.md").write_text("x", encoding="utf-8")
    assert choose_record_stem(tmp_path, "6483275", dt) == "2026-08-27_09-37_6483275"


def test_final_archive_requires_real_drive_urls():
    with pytest.raises(SystemExit):
        require_real_drive_urls("", "", prepare_only=False)


def test_real_drive_urls_are_accepted():
    require_real_drive_urls(
        "https://docs.google.com/presentation/d/example/edit",
        "https://drive.google.com/file/d/example/view",
        prepare_only=False,
    )


def test_prepare_only_is_not_final_completion():
    require_real_drive_urls("", "", prepare_only=True)


def test_parse_up_to_two_campuses():
    campuses = parse_campuses_json(
        '[{"name":"望江校区","latitude":"30.63","longitude":"104.08"},'
        '{"name":"江安校区","latitude":"30.56","longitude":"103.99"}]'
    )
    assert [c["name"] for c in campuses] == ["望江校区", "江安校区"]


def test_reject_more_than_two_campuses():
    raw = (
        '[{"name":"A","latitude":"1","longitude":"2"},'
        '{"name":"B","latitude":"3","longitude":"4"},'
        '{"name":"C","latitude":"5","longitude":"6"}]'
    )
    with pytest.raises(ValueError):
        parse_campuses_json(raw)
