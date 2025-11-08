#!/usr/bin/env python3
"""
main.py - 简单项目入口示例

提供几个方便的命令行选项用于验证仓库环境：
  --version    打印版本信息
  --list-files 列出当前目录下的文件（递归）
  --run        运行示例功能

这是一个小而安全的占位文件，你可以按需替换或扩展。
"""
from __future__ import annotations

import argparse
import os
import sys


VERSION = "2025-project v0.1"


def show_version() -> None:
	print(VERSION)


def list_files(path: str = ".") -> None:
	for root, _dirs, files in os.walk(path):
		for f in files:
			print(os.path.join(root, f))


def run_demo() -> None:
	print("Running demo function...")
	print("Current working directory:", os.getcwd())


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
	p = argparse.ArgumentParser(description="2025 project demo entrypoint")
	p.add_argument("--version", action="store_true", help="print version")
	p.add_argument("--list-files", action="store_true", help="recursively list files")
	p.add_argument("--run", action="store_true", help="run demo")
	return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
	args = parse_args(argv)
	if args.version:
		show_version()
		return 0
	if args.list_files:
		list_files()
		return 0
	if args.run:
		run_demo()
		return 0

	# 默认行为：打印帮助
	parse_args(["-h"])  # 打印并退出
	return 0


if __name__ == "__main__":
	raise SystemExit(main())