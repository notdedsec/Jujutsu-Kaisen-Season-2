import myaa.subkt.ass.*
import myaa.subkt.tasks.*
import myaa.subkt.tasks.Mux.*
import myaa.subkt.tasks.Nyaa.*
import java.awt.Color
import java.time.*

plugins {
    id("myaa.subkt")
}

subs {
    readProperties("sub.properties", "private.properties")
    release(arg("release") ?: "BD")
    episodes(getList("episodes"))

    merge {
        from(get("dialogue")) {
            incrementLayer(10)
        }

        from(getList("typesets"))

        if(propertyExists("opsync")) {
            from(get("OP")) {
                syncTargetTime(getAs<Duration>("opsync"))
            }
        }

        if(propertyExists("ecsync")) {
            from(get("EC")) {
                syncTargetTime(getAs<Duration>("ecsync"))
            }
        }

        if(propertyExists("exsync")) {
            from(get("EX")) {
                syncTargetTime(getAs<Duration>("exsync"))
            }
        }

        if(propertyExists("edsync")) {
            from(get("ED")) {
                syncTargetTime(getAs<Duration>("edsync"))
            }
        }

        if(propertyExists("insync")) {
            from(get("IN")) {
                syncTargetTime(getAs<Duration>("insync"))
            }
        }

        includeExtraData(false)
        includeProjectGarbage(false)

        out(get("out_merge"))
    }

    swap {
        from(merge.item())
        styles(Regex("Default|Alt|Cursed"))
        out(get("out_swap"))
    }

    chapters {
        from(swap.item())
        out(get("out_chapters"))
    }

    mux {
        title(get("title"))

        from(get("premux")) {
            tracks {
                lang("jpn")

                if(track.type == TrackType.VIDEO){
                    name("BD 1080p HEVC [dedsec]")
                }

                if(track.type == TrackType.AUDIO){
                    name("Japanese 2.0 AAC")
                }
            }

            attachments {
                include(false)
            }
        }

        from(merge.item()) {
            tracks {
                name("Kaizoku")
                lang("eng")
                default(true)
            }
        }

        from(swap.item()) {
            tracks {
                name("Kaizoku (Honorifics)")
                lang("enm")
            }
        }

        chapters(chapters.item()) {
            lang("eng")
            charset("UTF-8")
        }

        attach(get("fonts")) {
            includeExtensions("ttf", "otf")
        }

        skipUnusedFonts(true)
        out(get("muxfile"))
    }

    alltasks {
        torrent {
            from(mux.batchItems())

            if (isBatch) {
                into(get("muxbase"))
            }

            trackers(getList("tracker"))
            out(get("torrent"))
        }

        nyaa {
            from(torrent.item())
            username(get("nyaauser"))
            password(get("nyaapass"))
            torrentName(get("torrentname"))
            category(NyaaCategories.ANIME_ENGLISH)
            information(get("gitrepo"))
            torrentDescription(getFile("description.vm"))
            hidden(false)
        }
    }
}
