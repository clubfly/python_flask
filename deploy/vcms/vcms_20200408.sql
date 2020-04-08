--
-- PostgreSQL database dump
--

-- Dumped from database version 10.7 (Debian 10.7-1.pgdg90+1)
-- Dumped by pg_dump version 10.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: cube; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS cube WITH SCHEMA public;


--
-- Name: EXTENSION cube; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION cube IS 'data type for multidimensional cubes';


--
-- Name: euc_distance(double precision[], double precision[]); Type: FUNCTION; Schema: public; Owner: ent.prd
--

CREATE FUNCTION public.euc_distance(l double precision[], r double precision[]) RETURNS double precision
    LANGUAGE plpgsql
    AS $$  
DECLARE  
  s float8 := 0;  -- 中间结果   
  x float8;       -- LOOP中的数组元素值   
  i int := 1;     -- 数组下标   
  r_len int := array_length(r,1);    -- 右边数组的长度   
  l_len int := array_length(l,1);    -- 左边数组的长度   
BEGIN  
  if l_len >= r_len then  
    foreach x in array l LOOP  
      s := s + ( (x - case when i<=r_len then r[i] else 0 end) ^ 2 );  
      i := i+1;  
    END LOOP;  
  else  
    foreach x in array r LOOP  
      s := s + ( (x - case when i<=l_len then l[i] else 0 end) ^ 2 );  
      i := i+1;  
    END LOOP;  
  end if;  
  RETURN |/ s;  
END;  
$$;


ALTER FUNCTION public.euc_distance(l double precision[], r double precision[]) OWNER TO "ent.prd";

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: companies; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.companies (
    sn bigint NOT NULL,
    company_name character varying NOT NULL,
    max_admin_cnt integer DEFAULT 5 NOT NULL,
    max_branch_user_cnt integer DEFAULT 5 NOT NULL,
    max_branch_cnt integer DEFAULT 5 NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.companies OWNER TO "ent.prd";

--
-- Name: companies_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.companies_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.companies_sn_seq OWNER TO "ent.prd";

--
-- Name: companies_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.companies_sn_seq OWNED BY public.companies.sn;


--
-- Name: company_branch_products; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.company_branch_products (
    sn bigint NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    service_sn integer DEFAULT 0 NOT NULL,
    branch_sn integer DEFAULT 0 NOT NULL,
    product_sn integer DEFAULT 0 NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.company_branch_products OWNER TO "ent.prd";

--
-- Name: company_branch_products_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.company_branch_products_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_branch_products_sn_seq OWNER TO "ent.prd";

--
-- Name: company_branch_products_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.company_branch_products_sn_seq OWNED BY public.company_branch_products.sn;


--
-- Name: company_branches; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.company_branches (
    sn bigint NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    branch_name character varying,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.company_branches OWNER TO "ent.prd";

--
-- Name: company_branches_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.company_branches_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_branches_sn_seq OWNER TO "ent.prd";

--
-- Name: company_branches_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.company_branches_sn_seq OWNED BY public.company_branches.sn;


--
-- Name: company_product_csv; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.company_product_csv (
    sn bigint NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    user_file_name character varying NOT NULL,
    sys_file_name character varying NOT NULL,
    file_manage_mark integer DEFAULT 0 NOT NULL,
    file_manage_time timestamp without time zone,
    service_sn integer DEFAULT 0 NOT NULL,
    data_total integer DEFAULT 0 NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.company_product_csv OWNER TO "ent.prd";

--
-- Name: company_product_csv_contents; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.company_product_csv_contents (
    sn bigint NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    product_csv_sn integer DEFAULT 0 NOT NULL,
    sku character varying NOT NULL,
    barcode character varying,
    product_name character varying NOT NULL,
    ori_file_path character varying,
    sys_file_path character varying,
    url character varying,
    product_created_mark integer DEFAULT 0 NOT NULL,
    product_created_time timestamp without time zone,
    service_sn integer DEFAULT 0 NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.company_product_csv_contents OWNER TO "ent.prd";

--
-- Name: company_product_csv_contents_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.company_product_csv_contents_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_product_csv_contents_sn_seq OWNER TO "ent.prd";

--
-- Name: company_product_csv_contents_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.company_product_csv_contents_sn_seq OWNED BY public.company_product_csv_contents.sn;


--
-- Name: company_product_csv_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.company_product_csv_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_product_csv_sn_seq OWNER TO "ent.prd";

--
-- Name: company_product_csv_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.company_product_csv_sn_seq OWNED BY public.company_product_csv.sn;


--
-- Name: company_product_image_csv; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.company_product_image_csv (
    sn bigint NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    user_file_name character varying NOT NULL,
    sys_file_name character varying NOT NULL,
    file_manage_mark integer DEFAULT 0 NOT NULL,
    file_manage_time timestamp without time zone,
    service_sn integer DEFAULT 0 NOT NULL,
    data_total integer DEFAULT 0 NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL,
    zip_user_file_name character varying,
    zip_sys_file_name character varying,
    zip_manage_mark integer DEFAULT 0,
    zip_manage_time timestamp without time zone
);


ALTER TABLE public.company_product_image_csv OWNER TO "ent.prd";

--
-- Name: company_product_image_csv_contents; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.company_product_image_csv_contents (
    sn bigint NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    product_image_csv_sn integer DEFAULT 0 NOT NULL,
    sku character varying NOT NULL,
    product_name character varying NOT NULL,
    ori_file_path character varying,
    sys_file_path character varying,
    url character varying,
    image_created_mark integer DEFAULT 0 NOT NULL,
    image_created_time timestamp without time zone,
    service_sn integer DEFAULT 0 NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL,
    barcode character varying
);


ALTER TABLE public.company_product_image_csv_contents OWNER TO "ent.prd";

--
-- Name: company_product_image_csv_contents_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.company_product_image_csv_contents_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_product_image_csv_contents_sn_seq OWNER TO "ent.prd";

--
-- Name: company_product_image_csv_contents_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.company_product_image_csv_contents_sn_seq OWNED BY public.company_product_image_csv_contents.sn;


--
-- Name: company_product_image_csv_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.company_product_image_csv_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_product_image_csv_sn_seq OWNER TO "ent.prd";

--
-- Name: company_product_image_csv_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.company_product_image_csv_sn_seq OWNED BY public.company_product_image_csv.sn;


--
-- Name: company_product_image_features; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.company_product_image_features (
    sn bigint NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    service_sn integer DEFAULT 0 NOT NULL,
    product_sn integer DEFAULT 0 NOT NULL,
    image_sn integer DEFAULT 0 NOT NULL,
    x double precision DEFAULT 0 NOT NULL,
    y double precision DEFAULT 0 NOT NULL,
    w double precision DEFAULT 0 NOT NULL,
    h double precision DEFAULT 0 NOT NULL,
    feature double precision[],
    contour double precision[],
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
)
WITH (parallel_workers='32');


ALTER TABLE public.company_product_image_features OWNER TO "ent.prd";

--
-- Name: company_product_image_features_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.company_product_image_features_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_product_image_features_sn_seq OWNER TO "ent.prd";

--
-- Name: company_product_image_features_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.company_product_image_features_sn_seq OWNED BY public.company_product_image_features.sn;


--
-- Name: company_product_images; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.company_product_images (
    sn bigint NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    service_sn integer DEFAULT 0 NOT NULL,
    product_sn integer DEFAULT 0 NOT NULL,
    thumbnail character varying NOT NULL,
    feature_extraction_send_mark integer DEFAULT 0 NOT NULL,
    feature_extraction_send_time timestamp without time zone,
    feature_extraction_finish_mark integer DEFAULT 0 NOT NULL,
    feature_extraction_finish_time timestamp without time zone,
    bbox_totals integer DEFAULT 0 NOT NULL,
    detection_send_mark integer DEFAULT 0 NOT NULL,
    detection_send_time timestamp without time zone,
    detection_finish_mark integer DEFAULT 0 NOT NULL,
    detection_finish_time timestamp without time zone,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL,
    image_csv_sn integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.company_product_images OWNER TO "ent.prd";

--
-- Name: company_product_images_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.company_product_images_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_product_images_sn_seq OWNER TO "ent.prd";

--
-- Name: company_product_images_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.company_product_images_sn_seq OWNED BY public.company_product_images.sn;


--
-- Name: company_products; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.company_products (
    sn bigint NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    service_sn integer DEFAULT 0 NOT NULL,
    barcode character varying,
    sku character varying NOT NULL,
    product_name character varying NOT NULL,
    abbreviation character varying,
    thumbnail character varying NOT NULL,
    image_totals integer DEFAULT 0 NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL,
    product_csv_sn integer DEFAULT 0 NOT NULL,
    category character varying
);


ALTER TABLE public.company_products OWNER TO "ent.prd";

--
-- Name: company_products_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.company_products_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_products_sn_seq OWNER TO "ent.prd";

--
-- Name: company_products_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.company_products_sn_seq OWNED BY public.company_products.sn;


--
-- Name: company_profiles; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.company_profiles (
    sn bigint NOT NULL,
    company_sn integer NOT NULL,
    company_name character varying,
    company_no character varying,
    company_address character varying,
    company_tel character varying,
    company_contact character varying,
    company_contact_tel character varying,
    company_contact_email character varying,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.company_profiles OWNER TO "ent.prd";

--
-- Name: company_profiles_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.company_profiles_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_profiles_sn_seq OWNER TO "ent.prd";

--
-- Name: company_profiles_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.company_profiles_sn_seq OWNED BY public.company_profiles.sn;


--
-- Name: company_services; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.company_services (
    sn bigint NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    per_product_image_cnt integer DEFAULT 1000 NOT NULL,
    service_sn integer DEFAULT 0 NOT NULL,
    recognition_model_name character varying,
    recognition_model_version character varying,
    deploy_apply_mark integer DEFAULT 0 NOT NULL,
    deploy_apply_time timestamp without time zone,
    deploy_accept_mark integer DEFAULT 0 NOT NULL,
    deploy_accept_time timestamp without time zone,
    system_deploy_mark integer DEFAULT 0 NOT NULL,
    system_deploy_time timestamp without time zone,
    max_product_cnt integer DEFAULT 50 NOT NULL,
    min_training_cnt integer DEFAULT 10 NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL,
    detection_api character varying,
    feature_api character varying,
    self_test_api character varying,
    pkl_update_api character varying
);


ALTER TABLE public.company_services OWNER TO "ent.prd";

--
-- Name: company_services_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.company_services_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_services_sn_seq OWNER TO "ent.prd";

--
-- Name: company_services_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.company_services_sn_seq OWNED BY public.company_services.sn;


--
-- Name: feature_pkl_contents; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.feature_pkl_contents (
    sn bigint NOT NULL,
    feature_pkl_sn integer DEFAULT 0 NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    service_sn integer DEFAULT 0 NOT NULL,
    branch_sn integer DEFAULT 0 NOT NULL,
    pkl_key character varying NOT NULL,
    image_sn integer DEFAULT 0 NOT NULL,
    sku character varying NOT NULL,
    feature_sn integer DEFAULT 0 NOT NULL,
    product_sn integer DEFAULT 0 NOT NULL,
    product_name character varying,
    barcode character varying,
    feature double precision[],
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.feature_pkl_contents OWNER TO "ent.prd";

--
-- Name: feature_pkl_contents_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.feature_pkl_contents_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.feature_pkl_contents_sn_seq OWNER TO "ent.prd";

--
-- Name: feature_pkl_contents_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.feature_pkl_contents_sn_seq OWNED BY public.feature_pkl_contents.sn;


--
-- Name: feature_pkl_files; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.feature_pkl_files (
    sn bigint NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    service_sn integer DEFAULT 0 NOT NULL,
    branch_sn integer DEFAULT 0 NOT NULL,
    pkl_key character varying NOT NULL,
    pkl_update_send_mark integer DEFAULT 0 NOT NULL,
    pkl_update_send_time timestamp without time zone,
    pkl_update_finish_mark integer DEFAULT 0 NOT NULL,
    pkl_update_finish_time timestamp without time zone,
    output_pkl_mark integer DEFAULT 0 NOT NULL,
    output_pkl_time timestamp without time zone,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.feature_pkl_files OWNER TO "ent.prd";

--
-- Name: feature_pkl_files_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.feature_pkl_files_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.feature_pkl_files_sn_seq OWNER TO "ent.prd";

--
-- Name: feature_pkl_files_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.feature_pkl_files_sn_seq OWNED BY public.feature_pkl_files.sn;


--
-- Name: license_encrypt_types; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.license_encrypt_types (
    sn bigint NOT NULL,
    encrypt_type character varying NOT NULL,
    encrypt_name character varying NOT NULL,
    default_select integer DEFAULT 0 NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.license_encrypt_types OWNER TO "ent.prd";

--
-- Name: license_encrypt_types_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.license_encrypt_types_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.license_encrypt_types_sn_seq OWNER TO "ent.prd";

--
-- Name: license_encrypt_types_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.license_encrypt_types_sn_seq OWNED BY public.license_encrypt_types.sn;


--
-- Name: license_id_types; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.license_id_types (
    sn bigint NOT NULL,
    id_type character varying NOT NULL,
    id_name character varying NOT NULL,
    default_select integer DEFAULT 0 NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.license_id_types OWNER TO "ent.prd";

--
-- Name: license_id_types_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.license_id_types_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.license_id_types_sn_seq OWNER TO "ent.prd";

--
-- Name: license_id_types_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.license_id_types_sn_seq OWNED BY public.license_id_types.sn;


--
-- Name: license_requests; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.license_requests (
    sn bigint NOT NULL,
    company_sn bigint NOT NULL,
    company_name character varying NOT NULL,
    encrypt_sn bigint NOT NULL,
    encrypt_type character varying NOT NULL,
    service_sn bigint NOT NULL,
    service_name character varying NOT NULL,
    license_feature character varying NOT NULL,
    version character varying NOT NULL,
    trial_sn integer DEFAULT 0 NOT NULL,
    trial_type character varying NOT NULL,
    id_sn integer DEFAULT 0 NOT NULL,
    id_type character varying NOT NULL,
    hostid character varying NOT NULL,
    start_date character varying NOT NULL,
    expire_date character varying NOT NULL,
    connect_count character varying NOT NULL,
    server character varying NOT NULL,
    port character varying NOT NULL,
    license_count integer DEFAULT 0 NOT NULL,
    batch_license_count integer DEFAULT 0 NOT NULL,
    batch_update_send_mark integer DEFAULT 0 NOT NULL,
    batch_update_send_time timestamp without time zone,
    batch_update_finish_mark integer DEFAULT 0 NOT NULL,
    batch_update_finish_time timestamp without time zone,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.license_requests OWNER TO "ent.prd";

--
-- Name: license_requests_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.license_requests_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.license_requests_sn_seq OWNER TO "ent.prd";

--
-- Name: license_requests_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.license_requests_sn_seq OWNED BY public.license_requests.sn;


--
-- Name: license_trial_types; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.license_trial_types (
    sn bigint NOT NULL,
    trial_type character varying NOT NULL,
    trial_name character varying NOT NULL,
    trial_days integer DEFAULT 0 NOT NULL,
    default_select integer DEFAULT 0 NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.license_trial_types OWNER TO "ent.prd";

--
-- Name: license_trial_types_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.license_trial_types_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.license_trial_types_sn_seq OWNER TO "ent.prd";

--
-- Name: license_trial_types_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.license_trial_types_sn_seq OWNED BY public.license_trial_types.sn;


--
-- Name: licenses; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.licenses (
    sn bigint NOT NULL,
    license_key character varying NOT NULL,
    generate_type character varying NOT NULL,
    request_sn bigint NOT NULL,
    company_sn bigint NOT NULL,
    company_name character varying NOT NULL,
    encrypt_type character varying NOT NULL,
    license_feature character varying NOT NULL,
    version character varying NOT NULL,
    trial_type character varying NOT NULL,
    id_type character varying NOT NULL,
    hostid character varying NOT NULL,
    start_date character varying NOT NULL,
    expire_date character varying NOT NULL,
    connect_count character varying,
    server character varying,
    port character varying,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.licenses OWNER TO "ent.prd";

--
-- Name: licenses_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.licenses_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.licenses_sn_seq OWNER TO "ent.prd";

--
-- Name: licenses_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.licenses_sn_seq OWNED BY public.licenses.sn;


--
-- Name: system_announcement; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.system_announcement (
    sn bigint NOT NULL,
    board_hash character varying NOT NULL,
    publish_mark integer DEFAULT 0 NOT NULL,
    publish_time timestamp without time zone,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.system_announcement OWNER TO "ent.prd";

--
-- Name: system_announcement_details; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.system_announcement_details (
    sn bigint NOT NULL,
    board_hash character varying NOT NULL,
    language_type character varying NOT NULL,
    titles character varying NOT NULL,
    contents text NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.system_announcement_details OWNER TO "ent.prd";

--
-- Name: system_announcement_details_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.system_announcement_details_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.system_announcement_details_sn_seq OWNER TO "ent.prd";

--
-- Name: system_announcement_details_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.system_announcement_details_sn_seq OWNED BY public.system_announcement_details.sn;


--
-- Name: system_announcement_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.system_announcement_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.system_announcement_sn_seq OWNER TO "ent.prd";

--
-- Name: system_announcement_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.system_announcement_sn_seq OWNED BY public.system_announcement.sn;


--
-- Name: system_lock_upload_images; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.system_lock_upload_images (
    sn bigint NOT NULL,
    lock_token character varying NOT NULL,
    lock_mark integer DEFAULT 0 NOT NULL,
    lock_time timestamp without time zone,
    unlock_time timestamp without time zone,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.system_lock_upload_images OWNER TO "ent.prd";

--
-- Name: system_lock_upload_images_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.system_lock_upload_images_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.system_lock_upload_images_sn_seq OWNER TO "ent.prd";

--
-- Name: system_lock_upload_images_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.system_lock_upload_images_sn_seq OWNED BY public.system_lock_upload_images.sn;


--
-- Name: system_recognition_services; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.system_recognition_services (
    sn bigint NOT NULL,
    service_name character varying,
    service_type character varying,
    feature_extraction_mark integer DEFAULT 1 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.system_recognition_services OWNER TO "ent.prd";

--
-- Name: system_recognition_services_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.system_recognition_services_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.system_recognition_services_sn_seq OWNER TO "ent.prd";

--
-- Name: system_recognition_services_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.system_recognition_services_sn_seq OWNED BY public.system_recognition_services.sn;


--
-- Name: system_user_ranks; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.system_user_ranks (
    sn bigint NOT NULL,
    rank_name character varying NOT NULL,
    rank_function character varying NOT NULL,
    rank_js character varying NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.system_user_ranks OWNER TO "ent.prd";

--
-- Name: system_user_ranks_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.system_user_ranks_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.system_user_ranks_sn_seq OWNER TO "ent.prd";

--
-- Name: system_user_ranks_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.system_user_ranks_sn_seq OWNED BY public.system_user_ranks.sn;


--
-- Name: user_service_permissions; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.user_service_permissions (
    sn bigint NOT NULL,
    user_sn integer DEFAULT 0 NOT NULL,
    company_service_sn integer DEFAULT 0 NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    service_sn integer DEFAULT 0 NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.user_service_permissions OWNER TO "ent.prd";

--
-- Name: user_service_permissions_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.user_service_permissions_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_service_permissions_sn_seq OWNER TO "ent.prd";

--
-- Name: user_service_permissions_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.user_service_permissions_sn_seq OWNED BY public.user_service_permissions.sn;


--
-- Name: users; Type: TABLE; Schema: public; Owner: ent.prd
--

CREATE TABLE public.users (
    sn bigint NOT NULL,
    account character varying NOT NULL,
    passwords character varying NOT NULL,
    company_sn integer DEFAULT 0 NOT NULL,
    lock_mark integer DEFAULT 0 NOT NULL,
    lock_time timestamp without time zone,
    lock_reason character varying,
    user_rank_sn integer DEFAULT 3 NOT NULL,
    last_login_time timestamp without time zone,
    company_branch_sn integer DEFAULT 0 NOT NULL,
    ct_user_sn integer DEFAULT 0 NOT NULL,
    ut_user_sn integer DEFAULT 0 NOT NULL,
    enabled integer DEFAULT 1 NOT NULL,
    ct timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ut timestamp without time zone,
    deprecated integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.users OWNER TO "ent.prd";

--
-- Name: users_sn_seq; Type: SEQUENCE; Schema: public; Owner: ent.prd
--

CREATE SEQUENCE public.users_sn_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_sn_seq OWNER TO "ent.prd";

--
-- Name: users_sn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ent.prd
--

ALTER SEQUENCE public.users_sn_seq OWNED BY public.users.sn;


--
-- Name: companies sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.companies ALTER COLUMN sn SET DEFAULT nextval('public.companies_sn_seq'::regclass);


--
-- Name: company_branch_products sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_branch_products ALTER COLUMN sn SET DEFAULT nextval('public.company_branch_products_sn_seq'::regclass);


--
-- Name: company_branches sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_branches ALTER COLUMN sn SET DEFAULT nextval('public.company_branches_sn_seq'::regclass);


--
-- Name: company_product_csv sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_product_csv ALTER COLUMN sn SET DEFAULT nextval('public.company_product_csv_sn_seq'::regclass);


--
-- Name: company_product_csv_contents sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_product_csv_contents ALTER COLUMN sn SET DEFAULT nextval('public.company_product_csv_contents_sn_seq'::regclass);


--
-- Name: company_product_image_csv sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_product_image_csv ALTER COLUMN sn SET DEFAULT nextval('public.company_product_image_csv_sn_seq'::regclass);


--
-- Name: company_product_image_csv_contents sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_product_image_csv_contents ALTER COLUMN sn SET DEFAULT nextval('public.company_product_image_csv_contents_sn_seq'::regclass);


--
-- Name: company_product_image_features sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_product_image_features ALTER COLUMN sn SET DEFAULT nextval('public.company_product_image_features_sn_seq'::regclass);


--
-- Name: company_product_images sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_product_images ALTER COLUMN sn SET DEFAULT nextval('public.company_product_images_sn_seq'::regclass);


--
-- Name: company_products sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_products ALTER COLUMN sn SET DEFAULT nextval('public.company_products_sn_seq'::regclass);


--
-- Name: company_profiles sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_profiles ALTER COLUMN sn SET DEFAULT nextval('public.company_profiles_sn_seq'::regclass);


--
-- Name: company_services sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_services ALTER COLUMN sn SET DEFAULT nextval('public.company_services_sn_seq'::regclass);


--
-- Name: feature_pkl_contents sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.feature_pkl_contents ALTER COLUMN sn SET DEFAULT nextval('public.feature_pkl_contents_sn_seq'::regclass);


--
-- Name: feature_pkl_files sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.feature_pkl_files ALTER COLUMN sn SET DEFAULT nextval('public.feature_pkl_files_sn_seq'::regclass);


--
-- Name: license_encrypt_types sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.license_encrypt_types ALTER COLUMN sn SET DEFAULT nextval('public.license_encrypt_types_sn_seq'::regclass);


--
-- Name: license_id_types sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.license_id_types ALTER COLUMN sn SET DEFAULT nextval('public.license_id_types_sn_seq'::regclass);


--
-- Name: license_requests sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.license_requests ALTER COLUMN sn SET DEFAULT nextval('public.license_requests_sn_seq'::regclass);


--
-- Name: license_trial_types sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.license_trial_types ALTER COLUMN sn SET DEFAULT nextval('public.license_trial_types_sn_seq'::regclass);


--
-- Name: licenses sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.licenses ALTER COLUMN sn SET DEFAULT nextval('public.licenses_sn_seq'::regclass);


--
-- Name: system_announcement sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.system_announcement ALTER COLUMN sn SET DEFAULT nextval('public.system_announcement_sn_seq'::regclass);


--
-- Name: system_announcement_details sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.system_announcement_details ALTER COLUMN sn SET DEFAULT nextval('public.system_announcement_details_sn_seq'::regclass);


--
-- Name: system_lock_upload_images sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.system_lock_upload_images ALTER COLUMN sn SET DEFAULT nextval('public.system_lock_upload_images_sn_seq'::regclass);


--
-- Name: system_recognition_services sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.system_recognition_services ALTER COLUMN sn SET DEFAULT nextval('public.system_recognition_services_sn_seq'::regclass);


--
-- Name: system_user_ranks sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.system_user_ranks ALTER COLUMN sn SET DEFAULT nextval('public.system_user_ranks_sn_seq'::regclass);


--
-- Name: user_service_permissions sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.user_service_permissions ALTER COLUMN sn SET DEFAULT nextval('public.user_service_permissions_sn_seq'::regclass);


--
-- Name: users sn; Type: DEFAULT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.users ALTER COLUMN sn SET DEFAULT nextval('public.users_sn_seq'::regclass);


--
-- Name: companies companies_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_pkey PRIMARY KEY (sn);


--
-- Name: company_branch_products company_branch_products_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_branch_products
    ADD CONSTRAINT company_branch_products_pkey PRIMARY KEY (sn);


--
-- Name: company_branches company_branches_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_branches
    ADD CONSTRAINT company_branches_pkey PRIMARY KEY (sn);


--
-- Name: company_product_csv_contents company_product_csv_contents_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_product_csv_contents
    ADD CONSTRAINT company_product_csv_contents_pkey PRIMARY KEY (sn);


--
-- Name: company_product_csv company_product_csv_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_product_csv
    ADD CONSTRAINT company_product_csv_pkey PRIMARY KEY (sn);


--
-- Name: company_product_image_csv_contents company_product_image_csv_contents_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_product_image_csv_contents
    ADD CONSTRAINT company_product_image_csv_contents_pkey PRIMARY KEY (sn);


--
-- Name: company_product_image_csv company_product_image_csv_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_product_image_csv
    ADD CONSTRAINT company_product_image_csv_pkey PRIMARY KEY (sn);


--
-- Name: company_product_image_features company_product_image_features_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_product_image_features
    ADD CONSTRAINT company_product_image_features_pkey PRIMARY KEY (sn);


--
-- Name: company_product_images company_product_images_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_product_images
    ADD CONSTRAINT company_product_images_pkey PRIMARY KEY (sn);


--
-- Name: company_products company_products_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_products
    ADD CONSTRAINT company_products_pkey PRIMARY KEY (sn);


--
-- Name: company_profiles company_profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_profiles
    ADD CONSTRAINT company_profiles_pkey PRIMARY KEY (sn);


--
-- Name: company_services company_services_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.company_services
    ADD CONSTRAINT company_services_pkey PRIMARY KEY (sn);


--
-- Name: feature_pkl_contents feature_pkl_contents_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.feature_pkl_contents
    ADD CONSTRAINT feature_pkl_contents_pkey PRIMARY KEY (sn);


--
-- Name: feature_pkl_files feature_pkl_files_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.feature_pkl_files
    ADD CONSTRAINT feature_pkl_files_pkey PRIMARY KEY (sn);


--
-- Name: license_encrypt_types license_encrypt_types_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.license_encrypt_types
    ADD CONSTRAINT license_encrypt_types_pkey PRIMARY KEY (sn);


--
-- Name: license_id_types license_id_types_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.license_id_types
    ADD CONSTRAINT license_id_types_pkey PRIMARY KEY (sn);


--
-- Name: license_requests license_requests_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.license_requests
    ADD CONSTRAINT license_requests_pkey PRIMARY KEY (sn);


--
-- Name: license_trial_types license_trial_types_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.license_trial_types
    ADD CONSTRAINT license_trial_types_pkey PRIMARY KEY (sn);


--
-- Name: licenses licenses_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.licenses
    ADD CONSTRAINT licenses_pkey PRIMARY KEY (sn);


--
-- Name: system_announcement_details system_announcement_details_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.system_announcement_details
    ADD CONSTRAINT system_announcement_details_pkey PRIMARY KEY (sn);


--
-- Name: system_announcement system_announcement_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.system_announcement
    ADD CONSTRAINT system_announcement_pkey PRIMARY KEY (sn);


--
-- Name: system_lock_upload_images system_lock_upload_images_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.system_lock_upload_images
    ADD CONSTRAINT system_lock_upload_images_pkey PRIMARY KEY (sn);


--
-- Name: system_recognition_services system_recognition_services_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.system_recognition_services
    ADD CONSTRAINT system_recognition_services_pkey PRIMARY KEY (sn);


--
-- Name: system_user_ranks system_user_ranks_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.system_user_ranks
    ADD CONSTRAINT system_user_ranks_pkey PRIMARY KEY (sn);


--
-- Name: user_service_permissions user_service_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.user_service_permissions
    ADD CONSTRAINT user_service_permissions_pkey PRIMARY KEY (sn);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: ent.prd
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (sn);


--
-- Name: company_branch_products_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_branch_products_key ON public.company_branch_products USING btree (company_sn);


--
-- Name: company_branch_products_key1; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_branch_products_key1 ON public.company_branch_products USING btree (service_sn);


--
-- Name: company_branch_products_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_branch_products_key2 ON public.company_branch_products USING btree (branch_sn);


--
-- Name: company_branch_products_key3; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_branch_products_key3 ON public.company_branch_products USING btree (product_sn);


--
-- Name: company_branch_products_key4; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_branch_products_key4 ON public.company_branch_products USING btree (ct_user_sn);


--
-- Name: company_branch_products_key5; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_branch_products_key5 ON public.company_branch_products USING btree (ut_user_sn);


--
-- Name: company_branch_products_key6; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_branch_products_key6 ON public.company_branch_products USING btree (enabled);


--
-- Name: company_branches_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_branches_key ON public.company_branches USING btree (company_sn);


--
-- Name: company_product_csv_contents_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_csv_contents_key ON public.company_product_csv_contents USING btree (company_sn);


--
-- Name: company_product_csv_contents_key1; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_csv_contents_key1 ON public.company_product_csv_contents USING btree (product_csv_sn);


--
-- Name: company_product_csv_contents_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_csv_contents_key2 ON public.company_product_csv_contents USING btree (product_created_mark);


--
-- Name: company_product_csv_contents_key3; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_csv_contents_key3 ON public.company_product_csv_contents USING btree (product_created_time);


--
-- Name: company_product_csv_contents_key4; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_csv_contents_key4 ON public.company_product_csv_contents USING btree (service_sn);


--
-- Name: company_product_csv_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_csv_key ON public.company_product_csv USING btree (company_sn);


--
-- Name: company_product_csv_key1; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_csv_key1 ON public.company_product_csv USING btree (file_manage_mark);


--
-- Name: company_product_csv_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_csv_key2 ON public.company_product_csv USING btree (file_manage_time);


--
-- Name: company_product_csv_key3; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_csv_key3 ON public.company_product_csv USING btree (service_sn);


--
-- Name: company_product_image_csv_contents_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_csv_contents_key ON public.company_product_image_csv_contents USING btree (company_sn);


--
-- Name: company_product_image_csv_contents_key1; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_csv_contents_key1 ON public.company_product_image_csv_contents USING btree (product_image_csv_sn);


--
-- Name: company_product_image_csv_contents_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_csv_contents_key2 ON public.company_product_image_csv_contents USING btree (sku);


--
-- Name: company_product_image_csv_contents_key3; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_csv_contents_key3 ON public.company_product_image_csv_contents USING btree (image_created_mark);


--
-- Name: company_product_image_csv_contents_key4; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_csv_contents_key4 ON public.company_product_image_csv_contents USING btree (image_created_time);


--
-- Name: company_product_image_csv_contents_key5; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_csv_contents_key5 ON public.company_product_image_csv_contents USING btree (service_sn);


--
-- Name: company_product_image_csv_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_csv_key ON public.company_product_image_csv USING btree (company_sn);


--
-- Name: company_product_image_csv_key1; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_csv_key1 ON public.company_product_image_csv USING btree (file_manage_mark);


--
-- Name: company_product_image_csv_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_csv_key2 ON public.company_product_image_csv USING btree (file_manage_time);


--
-- Name: company_product_image_csv_key3; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_csv_key3 ON public.company_product_image_csv USING btree (service_sn);


--
-- Name: company_product_image_features_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_features_key ON public.company_product_image_features USING btree (company_sn);


--
-- Name: company_product_image_features_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_features_key2 ON public.company_product_image_features USING btree (service_sn);


--
-- Name: company_product_image_features_key3; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_features_key3 ON public.company_product_image_features USING btree (product_sn);


--
-- Name: company_product_image_features_key4; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_features_key4 ON public.company_product_image_features USING btree (image_sn);


--
-- Name: company_product_image_features_key5; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_features_key5 ON public.company_product_image_features USING gin (feature);


--
-- Name: company_product_image_features_key6; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_image_features_key6 ON public.company_product_image_features USING btree (enabled);


--
-- Name: company_product_images_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_images_key ON public.company_product_images USING btree (company_sn);


--
-- Name: company_product_images_key1; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_images_key1 ON public.company_product_images USING btree (service_sn);


--
-- Name: company_product_images_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_images_key2 ON public.company_product_images USING btree (product_sn);


--
-- Name: company_product_images_key3; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_images_key3 ON public.company_product_images USING btree (feature_extraction_send_mark);


--
-- Name: company_product_images_key4; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_images_key4 ON public.company_product_images USING btree (feature_extraction_finish_mark);


--
-- Name: company_product_images_key5; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_images_key5 ON public.company_product_images USING btree (detection_send_mark);


--
-- Name: company_product_images_key6; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_images_key6 ON public.company_product_images USING btree (detection_finish_mark);


--
-- Name: company_product_images_key7; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_images_key7 ON public.company_product_images USING btree (enabled);


--
-- Name: company_product_images_key8; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_images_key8 ON public.company_product_images USING btree (deprecated);


--
-- Name: company_product_images_key9; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_product_images_key9 ON public.company_product_images USING btree (image_csv_sn);


--
-- Name: company_products_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_products_key ON public.company_products USING btree (company_sn);


--
-- Name: company_products_key1; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_products_key1 ON public.company_products USING btree (service_sn);


--
-- Name: company_products_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_products_key2 ON public.company_products USING btree (barcode);


--
-- Name: company_products_key3; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_products_key3 ON public.company_products USING btree (sku);


--
-- Name: company_products_key4; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_products_key4 ON public.company_products USING btree (ct_user_sn);


--
-- Name: company_products_key5; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_products_key5 ON public.company_products USING btree (ut_user_sn);


--
-- Name: company_products_key6; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_products_key6 ON public.company_products USING btree (enabled);


--
-- Name: company_profiles_ukey; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE UNIQUE INDEX company_profiles_ukey ON public.company_profiles USING btree (company_sn);


--
-- Name: company_services_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_services_key ON public.company_services USING btree (company_sn);


--
-- Name: company_services_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_services_key2 ON public.company_services USING btree (per_product_image_cnt);


--
-- Name: company_services_key3; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX company_services_key3 ON public.company_services USING btree (service_sn);


--
-- Name: feature_pkl_contents_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX feature_pkl_contents_key ON public.feature_pkl_contents USING btree (feature_pkl_sn);


--
-- Name: feature_pkl_contents_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX feature_pkl_contents_key2 ON public.feature_pkl_contents USING btree (company_sn);


--
-- Name: feature_pkl_contents_key3; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX feature_pkl_contents_key3 ON public.feature_pkl_contents USING btree (service_sn);


--
-- Name: feature_pkl_contents_key4; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX feature_pkl_contents_key4 ON public.feature_pkl_contents USING btree (branch_sn);


--
-- Name: feature_pkl_contents_key5; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX feature_pkl_contents_key5 ON public.feature_pkl_contents USING btree (pkl_key);


--
-- Name: feature_pkl_contents_key6; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX feature_pkl_contents_key6 ON public.feature_pkl_contents USING btree (sku);


--
-- Name: feature_pkl_files_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX feature_pkl_files_key ON public.feature_pkl_files USING btree (company_sn);


--
-- Name: feature_pkl_files_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX feature_pkl_files_key2 ON public.feature_pkl_files USING btree (service_sn);


--
-- Name: feature_pkl_files_key3; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX feature_pkl_files_key3 ON public.feature_pkl_files USING btree (branch_sn);


--
-- Name: feature_pkl_files_key4; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX feature_pkl_files_key4 ON public.feature_pkl_files USING btree (pkl_key);


--
-- Name: system_announcement_details_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX system_announcement_details_key ON public.system_announcement_details USING btree (board_hash);


--
-- Name: system_announcement_details_key1; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX system_announcement_details_key1 ON public.system_announcement_details USING btree (language_type);


--
-- Name: system_announcement_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE UNIQUE INDEX system_announcement_key ON public.system_announcement USING btree (board_hash);


--
-- Name: system_announcement_key1; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX system_announcement_key1 ON public.system_announcement USING btree (publish_mark);


--
-- Name: system_announcement_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX system_announcement_key2 ON public.system_announcement USING btree (publish_time);


--
-- Name: system_lock_upload_images_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE UNIQUE INDEX system_lock_upload_images_key ON public.system_lock_upload_images USING btree (lock_token);


--
-- Name: user_service_permissions_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX user_service_permissions_key ON public.user_service_permissions USING btree (user_sn);


--
-- Name: user_service_permissions_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX user_service_permissions_key2 ON public.user_service_permissions USING btree (company_service_sn);


--
-- Name: user_service_permissions_key3; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX user_service_permissions_key3 ON public.user_service_permissions USING btree (company_sn);


--
-- Name: user_service_permissions_key4; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX user_service_permissions_key4 ON public.user_service_permissions USING btree (service_sn);


--
-- Name: users_key; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX users_key ON public.users USING btree (company_sn);


--
-- Name: users_key2; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE INDEX users_key2 ON public.users USING btree (user_rank_sn);


--
-- Name: users_ukey; Type: INDEX; Schema: public; Owner: ent.prd
--

CREATE UNIQUE INDEX users_ukey ON public.users USING btree (account);


--
-- Name: FUNCTION cube_in(cstring); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_in(cstring) TO "ent.prd";


--
-- Name: FUNCTION cube_out(public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_out(public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube(double precision[]); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube(double precision[]) TO "ent.prd";


--
-- Name: FUNCTION cube(double precision); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube(double precision) TO "ent.prd";


--
-- Name: FUNCTION cube(double precision[], double precision[]); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube(double precision[], double precision[]) TO "ent.prd";


--
-- Name: FUNCTION cube(double precision, double precision); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube(double precision, double precision) TO "ent.prd";


--
-- Name: FUNCTION cube(public.cube, double precision); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube(public.cube, double precision) TO "ent.prd";


--
-- Name: FUNCTION cube(public.cube, double precision, double precision); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube(public.cube, double precision, double precision) TO "ent.prd";


--
-- Name: FUNCTION cube_cmp(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_cmp(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_contained(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_contained(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_contains(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_contains(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_coord(public.cube, integer); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_coord(public.cube, integer) TO "ent.prd";


--
-- Name: FUNCTION cube_coord_llur(public.cube, integer); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_coord_llur(public.cube, integer) TO "ent.prd";


--
-- Name: FUNCTION cube_dim(public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_dim(public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_distance(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_distance(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_enlarge(public.cube, double precision, integer); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_enlarge(public.cube, double precision, integer) TO "ent.prd";


--
-- Name: FUNCTION cube_eq(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_eq(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_ge(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_ge(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_gt(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_gt(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_inter(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_inter(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_is_point(public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_is_point(public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_le(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_le(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_ll_coord(public.cube, integer); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_ll_coord(public.cube, integer) TO "ent.prd";


--
-- Name: FUNCTION cube_lt(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_lt(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_ne(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_ne(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_overlap(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_overlap(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_size(public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_size(public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_subset(public.cube, integer[]); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_subset(public.cube, integer[]) TO "ent.prd";


--
-- Name: FUNCTION cube_union(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_union(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION cube_ur_coord(public.cube, integer); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.cube_ur_coord(public.cube, integer) TO "ent.prd";


--
-- Name: FUNCTION distance_chebyshev(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.distance_chebyshev(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION distance_taxicab(public.cube, public.cube); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.distance_taxicab(public.cube, public.cube) TO "ent.prd";


--
-- Name: FUNCTION g_cube_compress(internal); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.g_cube_compress(internal) TO "ent.prd";


--
-- Name: FUNCTION g_cube_consistent(internal, public.cube, smallint, oid, internal); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.g_cube_consistent(internal, public.cube, smallint, oid, internal) TO "ent.prd";


--
-- Name: FUNCTION g_cube_decompress(internal); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.g_cube_decompress(internal) TO "ent.prd";


--
-- Name: FUNCTION g_cube_distance(internal, public.cube, smallint, oid, internal); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.g_cube_distance(internal, public.cube, smallint, oid, internal) TO "ent.prd";


--
-- Name: FUNCTION g_cube_penalty(internal, internal, internal); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.g_cube_penalty(internal, internal, internal) TO "ent.prd";


--
-- Name: FUNCTION g_cube_picksplit(internal, internal); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.g_cube_picksplit(internal, internal) TO "ent.prd";


--
-- Name: FUNCTION g_cube_same(public.cube, public.cube, internal); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.g_cube_same(public.cube, public.cube, internal) TO "ent.prd";


--
-- Name: FUNCTION g_cube_union(internal, internal); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.g_cube_union(internal, internal) TO "ent.prd";


--
-- PostgreSQL database dump complete
--

