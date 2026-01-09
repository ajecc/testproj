from clearml import Task
print(Task.running_locally())
from dataclasses import dataclass, field
import draccus

@dataclass
class DatasetConfig:
    type: str         # e.g. "hf", "s3", "local"
    id: str   # e.g. dataset name / path / uuid

@dataclass
class Config:
    dataset: DatasetConfig

@draccus.wrap()
def main(cfg: Config):
    task = Task.init("test", "test")
    print("dataset.type =", cfg.dataset.type)
    print("dataset.id   =", cfg.dataset.id)

if __name__ == "__main__":
    main()

