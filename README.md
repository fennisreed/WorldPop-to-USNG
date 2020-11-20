# WorldPop-to-USNG
This is a brief script used to translate a WorldPop gridded population estimate to the US National Grid. Two inputs are required including a WorldPop 100m population raster, and a feature class of the desired output USNG cells (>=1km). The result adds a new field to the USNG feature class containing the corresponding population estimate. Because this is a quick and dirty translation, cetroids of each grid cell are aggregated to the greater unit. 

#### Dependencies:
Written in Python 2.7 using an ArcPy deployment from ArcMap 10.7. FME translation available on request.

#### Data:
- WorldPop 100m estimates can be downloaded by country from [here](https://www.worldpop.org/project/categories?id=3).
- USNG cells >= 1km can be downloaded at various resolutions [here](https://usngcenter.org/portfolio-item/usng-gis-data/).

#### Population Estimates Consideration: 
The real value of the WorldPop estimates is its population density. A variety of different population estimates are available from their website, which may be used to weight more recent population estimates estimates and projections. An example of such adjustment is available [here](https://github.com/wpgp/WPGP_adj_ppp_calc) from David Kerr.
As of 2020 the USNG now includes 100m cells. For estimates of finer resolution (<1km), I reccommend using a more spatially sensitive aggregation method.
