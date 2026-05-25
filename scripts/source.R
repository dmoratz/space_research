# =============================================================================
# source.R
# Shared setup file for Space Sci-Fi Analysis Pipeline
# =============================================================================
# This file contains:
# - Package loading
# - Custom functions
# - Global settings
# - Color palettes and themes
# =============================================================================

# -----------------------------------------------------------------------------
# Package Loading
# -----------------------------------------------------------------------------

# Use pacman for efficient package management
if (!require("pacman")) install.packages("pacman")

pacman::p_load(
  
  # Data manipulation
  
  tidyverse,
  dplyr,
  tidyr,
  purrr,
  data.table,
  lubridate,
  stringr,
  stringdist,
  readr,
  haven,
  foreign,
  
  
  # Visualization
  ggplot2,
  patchwork,
  cowplot,
  grid,
  gridExtra,
  scales,
  ggpubr,
  plotly,
  
  # Tables
  gt,
  knitr,
  kableExtra,
  modelsummary,
  stargazer,
  texreg,
  pander,
  
  # Statistical analysis
  estimatr,
  fixest,
  lfe,
  plm,
  sandwich,
  
  lmtest,
  rdrobust,
  AER,
  VGAM,
  
  # Other utilities
  here,
  broom,
  zoo,
  
  # Matching, sensitivity, and bootstrap
  fwildclusterboot,
  MatchIt,
  cobalt,
  rbounds,
  sensemakr,
  ggridges,
  
  # Spatial and inter-rater reliability
  rnaturalearth,
  rnaturalearthdata,
  sf,
  irr
)

# -----------------------------------------------------------------------------
# Global Settings
# -----------------------------------------------------------------------------

# Set seed for reproducibility
set.seed(3184)

# Scientific notation threshold
options(scipen = 3, digits = 3)