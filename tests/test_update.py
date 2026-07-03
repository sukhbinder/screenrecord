"""Tests for updated features in screenrecord: loop, save, fps, delay, duration, bbox, fullscreen, activewindow."""

import os
import tempfile
import subprocess
import shutil
from pathlib import Path
from screenrecord.srecord import create_parser, record, main_active, mainrun, main
from screenrecord import cli


def test_cli_parser_options():
    """Test that CLI parser includes all new options."""
    parser = create_parser()
    args = parser.parse_args(["test.gif"])

    # Test new options exist
    assert hasattr(args, "loop")
    assert hasattr(args, "fps")
    assert hasattr(args, "save")
    assert hasattr(args, "duration")

    # Test default values
    assert args.loop == 5  # Default loops for GIF
    assert args.fps == 10  # Default FPS
    assert args.save is False  # Default save is False


def test_loop_option():
    """Test loop parameter in record function."""
    # Test with different loop values
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, "test.gif")

        # Test default loop
        record(test_file, loop=5, initdelay=1, duration=2)
        assert os.path.exists(test_file)


def test_fps_option():
    """Test fps parameter in record function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, "test_fps.gif")

        # Test default FPS
        record(test_file, fps=10, initdelay=1, duration=2)
        assert os.path.exists(test_file)

        # Test custom FPS
        test_file2 = os.path.join(tmpdir, "test_fps2.gif")
        record(test_file2, fps=20, initdelay=1, duration=2)
        assert os.path.exists(test_file2)

        # Test low FPS
        test_file3 = os.path.join(tmpdir, "test_fps3.gif")
        record(test_file3, fps=5, initdelay=1, duration=2)
        assert os.path.exists(test_file3)


def test_delay_option():
    """Test delay parameter in record function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, "test_delay.gif")

        # Test default delay
        record(test_file, delay=0.1, initdelay=1, duration=2)
        assert os.path.exists(test_file)


def test_duration_option():
    """Test duration parameter in record function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, "test_duration.gif")

        # Test default duration (5 seconds)
        record(test_file, duration=5, initdelay=1)
        assert os.path.exists(test_file)


def test_fullscreen_option():
    """Test fullscreen parameter in CLI."""
    parser = create_parser()

    # Test fullscreen=True
    args1 = parser.parse_args(["test.gif", "-f"])
    assert args1.fullscreen is True

    # Test fullscreen=False (default)
    args2 = parser.parse_args(["test.gif"])
    assert args2.fullscreen is False

    # Test fullscreen with --fullscreen
    args3 = parser.parse_args(["test.gif", "--fullscreen"])
    assert args3.fullscreen is True


def test_activewindow_option():
    """Test activewindow parameter in CLI."""
    parser = create_parser()

    # Test activewindow=False (default)
    args1 = parser.parse_args(["test.gif"])
    assert args1.activewindow is False

    # Test activewindow=True
    args2 = parser.parse_args(["test.gif", "-aw"])
    assert args2.activewindow is True

    # Test activewindow with --activewindow
    args3 = parser.parse_args(["test.gif", "--activewindow"])
    assert args3.activewindow is True


def test_save_option():
    """Test save parameter in record function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_dir = os.path.join(tmpdir, "frames")
        os.makedirs(temp_dir, exist_ok=True)

        # Test save=True
        test_file = os.path.join(tmpdir, "test_save2.gif")
        record(test_file, save=True, initdelay=1, duration=2)
        assert os.path.exists(test_file)


def test_parser_argument_parsing():
    """Test that all new arguments are properly parsed."""
    parser = create_parser()

    # Test all arguments can be parsed
    args = parser.parse_args(
        [
            "test.gif",
            "-i",
            "10",  # initdelay
            "-d",
            "0.5",  # delay
            "-dur",
            "30",  # duration
            "--bbox",
            "100",
            "100",
            "200",
            "200",  # bbox
            "-f",  # fullscreen
            "-aw",  # activewindow
            "-s",  # save
            "--loop",
            "3",  # loop
            "--fps",
            "15",  # fps
        ]
    )

    assert args.initdelay == 10
    assert args.delay == 0.5
    assert args.duration == 30
    assert args.bbox == [100, 100, 200, 200]
    assert args.fullscreen is True
    assert args.activewindow is True
    assert args.save is True
    assert args.loop == 3
    assert args.fps == 15


def test_record_function_signature():
    """Test that record function has all required parameters."""
    import inspect

    sig = inspect.signature(record)
    params = list(sig.parameters.keys())

    required_params = [
        "outfilename",
        "initdelay",
        "delay",
        "duration",
        "area",
        "save",
        "fps",
        "loop",
    ]
    for param in required_params:
        assert param in params, f"Missing parameter: {param}"


def test_record_default_values():
    """Test that record function has sensible defaults."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, "test.gif")
        record(test_file, initdelay=1, duration=2)
        assert os.path.exists(test_file)


def test_record_with_all_options():
    """Test record function with all options specified."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, "test_all.gif")

        record(
            test_file,
            initdelay=1,
            delay=0.2,
            duration=5,
            area=[0, 0, 100, 100],
            save=False,
            fps=15,
            loop=3,
        )

        assert os.path.exists(test_file)


def test_cli_create_parser():
    """Test that cli.create_parser returns correct parser."""
    parser = cli.create_parser()
    assert parser.prog == "record"
    assert parser.description == "Screen Recording with python"


def test_cli_parse_args():
    """Test that cli can parse arguments correctly."""
    parser = cli.create_parser()
    args = parser.parse_args(["test.gif"])

    assert args.filename == "test.gif"
    assert args.initdelay == 5
    assert args.delay == 0.1
    assert args.duration == 20
    assert args.bbox == [0, 0, 50, 50]
    assert args.fullscreen is False
    assert args.activewindow is False
    assert args.loop == 5
    assert args.fps == 10
    assert args.save is False
