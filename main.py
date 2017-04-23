from sites import launchpad, transifex, translatewiki, weblate

language = "pl"

launchpad_projects = ["josm"]

transifex_projects = [
    ["nguillaumin", "osmtracker-android"],
    ["overpass-turbo", "overpass-turbo"],
    ["ideditor", "id-editor"],
    ["openstreetmap", "presets"],
    ["openstreetmap", "historic-objects-preset"],
    ["openstreetmap", "vespucci"],
    ["yohanboniface", "umap"],
    ["openstreetmap-france", "osmose"],
    ["osm-catala", "osmbot"],
    ["fieldpapers", "fieldpapers"]
]

translatewiki_projects = ["osm-potlatch2-main",
                          "out-waymarked-trails-0-all",
                          "out-osm-potlatch2-help",
                          "out-osm-site"]

weblate_projects = ["osmand/main", "osmand/phrases"]

results = []

results.extend(launchpad.run(launchpad_projects, language))
results.extend(transifex.run(transifex_projects, language))
results.extend(translatewiki.run(translatewiki_projects, language))
results.extend(weblate.run(weblate_projects, language))

print(results)
