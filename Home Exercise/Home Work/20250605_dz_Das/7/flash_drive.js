function start() {
    let flashDriveCapacityGB = 512;
    let fileSizeMB = 820;
    let GB_TO_MB = 1024;
    let flashDriveCapacityMB = flashDriveCapacityGB * GB_TO_MB;
    let numberOfFilesThatFit = Math.floor(flashDriveCapacityMB / fileSizeMB);

    console.log(`Flash Drive Capacity: ${flashDriveCapacityGB} GB (${flashDriveCapacityMB} MB)`);
    console.log(`File Size: ${fileSizeMB} MB`);
    console.log(`Number of files that fit: ${numberOfFilesThatFit}`);
}