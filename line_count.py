from pathlib import Path
from histogram import modules_to_buckets

def get_module_name(path: Path):
    if path.parent.name.startswith("@"):
        return path.parent.name+"/"+path.name
    else:
        return path.name

class ModuleMeta:
    def __init__(self, path: Path) -> None:
        lines = 0
        files = 0
        for file in path.glob("**/*"):
            if (
                file.is_file() and 
                not file.is_symlink() and 
                file.suffix in [".js", ".ts", ".mjs", ".cjs"]
            ):
                with open(file, encoding="utf-8") as opened_file:
                    contents = opened_file.read()
                    lines += max(contents.count("\n"), contents.count(";"))
                files += 1
        self.lines, self.files = lines, files
        self.path = path

    
    def __repr__(self) -> str:
        return (f"{get_module_name(self.path):50}: {self.lines:4} "
                f"lines of js/ts in {self.files:4} files")
    
    @property
    def module_name(self):
        return get_module_name(self.path)


def get_module_directories(path: Path) -> list[Path]:
    useful_dir = lambda x: x.is_dir() and x.name[0] != "."
    dirs = list(filter(useful_dir, path.iterdir()))
    for at_dir in filter(lambda x: x.name.startswith("@"), dirs):
        subdirs = list(filter(useful_dir, at_dir.iterdir()))
        dirs.remove(at_dir)
        dirs = subdirs + dirs
    return dirs

def get_meta(path: Path) -> list[ModuleMeta]:
    print("getting module directory list...")
    directories = get_module_directories(path)
    meta = []
    last_log_length = 0
    print()
    for i, directory in enumerate(directories):
        log = f"\ranalyzing {get_module_name(directory)} ({i+1} / {len(directories)})"
        log += " "*max(0, last_log_length-len(log))
        last_log_length = len(log)
        print(log, end="")
        meta.append(ModuleMeta(directory))
    print()
    meta.sort(key=lambda x: x.lines)
    return meta

if __name__ == "__main__":
    target = Path("C:/Users/Mitch/Documents/repositories/khe/singlehanded/node_modules/")
    # target = Path("C:/Users/Mitch/Documents/repositories/mod_analysis_test/node_modules")
    metas = get_meta(target)
    for meta in metas:
        print(meta)
    
    total_lines = total_files = 0
    for meta in metas:
        total_lines += meta.lines
        total_files += meta.files
    print(f"TOTAL LINES: {total_lines}")
    print(f"TOTAL FILES: {total_files}")

    with open(target.parent.name+".csv", "w+", encoding="utf-8") as csv_out:
        csv_out.write("module name,lines,files\n")
        for meta in metas:
            csv_out.write(f"{meta.module_name},{meta.lines},{meta.files}\n")
        csv_out.write(f"TOTAL,{total_lines},{total_files}\n")
    
    with open(target.parent.name+"_log_lines.csv", "w+", encoding="utf-8") as csv_out:
        csv_out.write("lines of js,modules with that many lines of js\n")
        for k,v in modules_to_buckets(metas).items():
            csv_out.write(f"{k},{v}\n")
    
    
