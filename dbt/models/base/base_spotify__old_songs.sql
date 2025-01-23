WITH source AS (
    SELECT
      *
    FROM {{ source('spotify', 'spotify_old_songs') }}
),

model AS (
    SELECT
        spotify_old_songs_id,
        spotify_old_songs_updated_at,
        spotify_old_songs_started_playing_at,
        spotify_old_songs_artist_name,
        spotify_old_songs_track_name,
        spotify_old_songs_album_name,
        spotify_old_songs_ms_player,
        spotify_old_songs_reason_start,
        spotify_old_songs_reason_end,
        spotify_old_songs_shuffle,
        spotify_old_songs_skipped,
        spotify_old_songs_offline,
        spotify_old_songs_track_id
    FROM source
)

SELECT * FROM model
