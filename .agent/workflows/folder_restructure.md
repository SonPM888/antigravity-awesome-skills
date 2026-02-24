---
description: Restructure the OneDrive workspace folder structure for BSC work
---

# Folder Restructure Workflow

## Overview
This workflow restructures the OneDrive workspace from a flat file dump into an organized business-function-based folder hierarchy.

## Pre-conditions
- Review `folder_review.md` artifact for context on current issues
- User must approve implementation plan before any file operations

## Steps

### Phase 1: Create Folder Structure (Safe — no file movement)
// turbo
1. Create the top-level folders:
   - `01_WORK_BSC/` — All BSC work files
   - `02_PERSONAL/` — Personal documents
   - `03_MEDIA/` — Pictures, Videos, Recordings
   - `04_PROJECTS/` — Side projects (YouTube, Python, Automation)
   - `05_REFERENCE/` — Templates, Regulations, Research

// turbo
2. Create `01_WORK_BSC/` sub-folders:
   - `01_HDQT/` with sub-folders: `Bien_ban`, `Nghi_quyet`, `Phieu_trinh`, `Quy_che`, `Thong_bao`
   - `02_NDD_BIDV/` with sub-folders: `Bao_cao_NDD`, `To_trinh`, `Phan_cap_uy_quyen`
   - `03_DHDCD/` with sub-folders by year
   - `04_FMC_EdR/` with sub-folders: `SCA`, `JVA`, `FMC_Timeline`, `Correspondence`
   - `05_HSC_Cooperation/`
   - `06_SMTB/`
   - `07_CBTT/`
   - `08_Strategy/` with sub-folders: `KHKD`, `Chien_luoc_26-30`
   - `09_KTNB/`
   - `10_IR/`
   - `11_VPHDQT/` with sub-folders: `KPI`, `Nhan_su`, `Quy_hoach`
   - `99_Archive/` with sub-folders by year

// turbo
3. Create `02_PERSONAL/` sub-folders:
   - `Dang/`, `Tai_chinh/`, `Gia_dinh/`, `Hoc_tap/`, `Du_lich/`

// turbo
4. Create `03_MEDIA/` sub-folders:
   - `Pictures/`, `Videos/`, `Recordings/`, `Screenshots/`

// turbo
5. Create `04_PROJECTS/` sub-folders:
   - `Youtube_Channel/`, `Python_PMS/`, `Automation/`

// turbo
6. Create `05_REFERENCE/` sub-folders:
   - `Templates/`, `Regulations/`, `Research/`

### Phase 2: Move Root Files (Requires user approval per batch)
7. Classify all root files by pattern (BB_, TTr, BC_, PT, NQ, etc.) and move them to appropriate folders under `01_WORK_BSC/`
8. Move personal files (Phiếu Bài Giảng, Menu, thẻ tín dụng, etc.) to `02_PERSONAL/`
9. Move media files to `03_MEDIA/`

### Phase 3: Move Documents Files
10. Apply the same classification logic to `Documents/` folder
11. Move files from `Documents/` sub-folders that overlap with the new structure

### Phase 4: Rename Files (Optional, batch by batch)
12. Rename files to follow the `YYMMDD_Type_Description_vX.Y` convention
13. Start with the most recent/active files first

### Phase 5: Cleanup
14. Remove empty original folders
15. Delete confirmed duplicate files (after user verification)

## File Naming Convention
```
[YYMMDD]_[Type]_[Description]_v[X.Y].[ext]
```
- Types: BB, NQ, TTr, BC, PT, CV, QC, TB
- Description: Vietnamese without diacritics, underscore-separated
- Version: v1, v2.1, etc.
- Status suffix: _DRAFT, _FINAL, _APPROVED

## Important Notes
- NEVER delete files without explicit user approval
- Always move (not copy) to avoid duplicates
- Phase 1 is completely safe (only creates empty folders)
- Each subsequent phase should be done in small batches with user review
