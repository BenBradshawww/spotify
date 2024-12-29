WITH source AS (
    SELECT
      *
    FROM {{ source('spotify', 'spotify_last_songs') }}
),

model AS (
    SELECT
        spotify_last_songs_id,
        spotify_last_songs_updated_at,
        spotify_last_songs_track_played_at,
        CASE
          WHEN spotify_last_songs_track_name = 'Unkown Track'
            THEN NULL
          ELSE spotify_last_songs_track_name
        END,
        CASE
          WHEN spotify_last_songs_artist_name = 'Unkown Artist'
            THEN NULL
          ELSE spotify_last_songs_artist_name
        END,
        spotify_last_songs_track_id
    FROM source
)

SELECT * FROM model
