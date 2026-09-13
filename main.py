from config import AppConfig

# Chargement de la configuration locale (dev)
config = AppConfig.load("app_config.yml", env="dev")

print("=== EXÉCUTION LOCALE ===")
print(f"Application      : {config.app_name}")
print(f"Catalogue utilisé: {config.catalog_name}")
print(f"Schéma utilisé   : {config.schema_name}")
