# WORLDPOP TO USNG CONVERSION
# ---------------------------------------------------------------------------
# DESCRIPTION: A brief script that converts WorldPop gridded population
# estimates to USNG grid cells. Centroids of each intersecting cell from the
# WP estimate are summed for each input geography and joined to the input feature.
# ---------------------------------------------------------------------------
# REQUIREMENTS: Python 2.7, ArcMap (Desktop 10.7+)
# WorldPop Constrained 100m PPP (persons per pixel) downloads can be found here:
# https://www.worldpop.org/project/categories?id=3
# USNG grids at various scales may be found here:
# https://usngcenter.org/portfolio-item/usng-gis-data/
# ---------------------------------------------------------------------------
# NOTES: If interested in a smaller subset area, I recommend breaking apart the USNG download to improve performance.
# Due to the nature of this method, smaller areas may be run and rejoined without conflict. For this I
# recommend subsets contain contiguous cells instead of random or widely spaced cells.
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Variable Paths
arcpy.env.workspace = "Workspace.gdb"
Worldpop = "WORLDPOP.tif"
USNG = "USNG_Input.shp"

# Process: Workflow - add WorldPop Population field to USNG input as SUM_grid_code
arcpy.Clip_management(Worldpop, "", "WP_Clip", USNG, "-9.999900e+04", "NONE", "NO_MAINTAIN_EXTENT")
arcpy.RasterToPoint_conversion("WP_Clip", "WP_Points")
arcpy.SpatialJoin_analysis("WP_Points", USNG, "WP_Join", "JOIN_ONE_TO_ONE", "KEEP_ALL", "", "WITHIN", "", "")
arcpy.MakeFeatureLayer_management("WP_Join", "WP_Join_Layer", "USNG IS NOT NULL")
arcpy.Statistics_analysis("WP_Join_Layer", "WP_Statistics", "grid_code SUM", "USNG")
arcpy.JoinField_management(USNG, "USNG", "WP_Statistics", "USNG", "SUM_grid_code")

# Process: Purge - remove intermediate features
arcpy.Delete_management("WP_Clip")
arcpy.Delete_management("WP_Points")
arcpy.Delete_management("WP_Join")
arcpy.Delete_management("WP_Join_Layer")
arcpy.Delete_management("WP_Statistics")
