from dataclasses import dataclass
import yaml

@dataclass
class AppConfig:
    app_name: str
    catalog_name: str
    schema_name: str

    @classmethod
    def load(cls, file_path: str = "config/project_config_youssouf.yml", env: str = "dev") -> "AppConfig":
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)

        return cls(
            app_name=data["app_name"],
            catalog_name=data[env]["catalog_name"],
            schema_name=data[env]["schema_name"],
        )
