-- Table: public.phone_providers

-- DROP TABLE IF EXISTS public.phone_providers;

CREATE TABLE IF NOT EXISTS public.phone_providers
(
    ndc integer NOT NULL,
    "snA" numeric NOT NULL,
    "snB" numeric NOT NULL,
    capacity integer,
    provider text COLLATE pg_catalog."default",
    region text COLLATE pg_catalog."default",
    territory_gar text COLLATE pg_catalog."default",
    inn numeric
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.phone_providers
    OWNER to postgres;

GRANT ALL ON TABLE public.phone_providers TO postgres;

GRANT ALL ON TABLE public.phone_providers TO super_user WITH GRANT OPTION;
-- Index: idx_unique_provider

-- DROP INDEX IF EXISTS public.idx_unique_provider;

CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_provider
    ON public.phone_providers USING btree
    (ndc ASC NULLS LAST, "snA" ASC NULLS LAST, "snB" ASC NULLS LAST)
    TABLESPACE pg_default;