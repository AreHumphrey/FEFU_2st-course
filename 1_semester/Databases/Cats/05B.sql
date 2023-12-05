WITH RECURSIVE ShowITEmployees AS (
    SELECT id, object_name, parent_id, extension, object_type, object_name || ':' AS full_path

    FROM windows_fs_table
    WHERE parent_id IS NULL
    UNION
    SELECT Win.id, Win.object_name, Win.parent_id, Show.extension, Show.object_type,
    CASE
        WHEN Win.extension IS NOT NULL THEN Show.full_path || '' || Win.object_name || '.' || Win.extension
        WHEN Show.parent_id IS NULL THEN Show.full_path || '\' ||  Win.object_name || '\'
        ELSE Show.full_path || '' || Win.object_name || '\'
    END
    FROM windows_fs_table Win
    JOIN ShowITEmployees Show ON Show.id = Win.parent_id
)
SELECT full_path AS full_name
FROM ShowITEmployees
ORDER BY ShowITEmployees.id
