SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;


CREATE SEQUENCE public.cms_messages_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cms_messages_seq OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;


CREATE TABLE public.cms_messages (
    message_id integer DEFAULT nextval('public.cms_messages_seq'::regclass) NOT NULL,
    full_name character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    message text NOT NULL,
    module character varying(255) DEFAULT 'data_analysis'::character varying NOT NULL,
    date_sent timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    date_responded timestamp(0) without time zone DEFAULT NULL::timestamp without time zone,
    status integer,
    locked integer DEFAULT 0,
    CONSTRAINT cms_messages_message_id_check CHECK ((message_id > 0))
);


ALTER TABLE public.cms_messages OWNER TO postgres;


CREATE SEQUENCE public.ds_applications_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_applications_seq OWNER TO postgres;


CREATE TABLE public.ds_applications (
    id integer DEFAULT nextval('public.ds_applications_seq'::regclass) NOT NULL,
    category_id integer DEFAULT 0 NOT NULL,
    application character varying(255) NOT NULL,
    created_time timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ds_applications OWNER TO postgres;


CREATE SEQUENCE public.ds_applications_categories_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_applications_categories_seq OWNER TO postgres;


CREATE TABLE public.ds_applications_categories (
    id integer DEFAULT nextval('public.ds_applications_categories_seq'::regclass) NOT NULL,
    category character varying(255) NOT NULL,
    created_time timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ds_applications_categories OWNER TO postgres;


CREATE SEQUENCE public.ds_books_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_books_seq OWNER TO postgres;


CREATE TABLE public.ds_books (
    id integer DEFAULT nextval('public.ds_books_seq'::regclass) NOT NULL,
    title character varying(255) NOT NULL,
    description text NOT NULL,
    CONSTRAINT ds_books_id_check CHECK ((id > 0))
);


ALTER TABLE public.ds_books OWNER TO postgres;


CREATE SEQUENCE public.ds_books_pages_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_books_pages_seq OWNER TO postgres;


CREATE TABLE public.ds_books_pages (
    id integer DEFAULT nextval('public.ds_books_pages_seq'::regclass) NOT NULL,
    bookid integer DEFAULT 0 NOT NULL,
    content text NOT NULL,
    CONSTRAINT ds_books_pages_bookid_check CHECK ((bookid > 0)),
    CONSTRAINT ds_books_pages_id_check CHECK ((id > 0))
);


ALTER TABLE public.ds_books_pages OWNER TO postgres;


CREATE SEQUENCE public.ds_business_listings_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_business_listings_seq OWNER TO postgres;


CREATE TABLE public.ds_business_listings (
    id integer DEFAULT nextval('public.ds_business_listings_seq'::regclass) NOT NULL,
    author_id integer DEFAULT 0 NOT NULL,
    url character varying(255) DEFAULT ''::character varying NOT NULL,
    contact_info character varying(255) DEFAULT ''::character varying NOT NULL,
    description text NOT NULL,
    submissiondate timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT ds_business_listings_author_id_check CHECK ((author_id > 0)),
    CONSTRAINT ds_business_listings_id_check CHECK ((id > 0))
);


ALTER TABLE public.ds_business_listings OWNER TO postgres;


CREATE SEQUENCE public.ds_emergingtopics_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_emergingtopics_seq OWNER TO postgres;


CREATE TABLE public.ds_emergingtopics (
    id integer DEFAULT nextval('public.ds_emergingtopics_seq'::regclass) NOT NULL,
    topicname character varying(255) NOT NULL,
    created_time timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ds_emergingtopics OWNER TO postgres;


CREATE SEQUENCE public.ds_goals_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_goals_seq OWNER TO postgres;


CREATE TABLE public.ds_goals (
    id integer DEFAULT nextval('public.ds_goals_seq'::regclass) NOT NULL,
    creator_id integer DEFAULT 0 NOT NULL,
    goal character varying(255) DEFAULT ''::character varying NOT NULL,
    submissiondate timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    startdate timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    enddate timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ds_goals OWNER TO postgres;


CREATE SEQUENCE public.ds_organizations_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_organizations_seq OWNER TO postgres;


CREATE TABLE public.ds_organizations (
    id integer DEFAULT nextval('public.ds_organizations_seq'::regclass) NOT NULL,
    organization_name character varying(255) DEFAULT ''::character varying NOT NULL,
    organization_url character varying(255) DEFAULT ''::character varying NOT NULL,
    organization_description text NOT NULL,
    submissiondate timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT ds_organizations_id_check CHECK ((id > 0))
);


ALTER TABLE public.ds_organizations OWNER TO postgres;


CREATE SEQUENCE public.ds_posts_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_posts_seq OWNER TO postgres;


CREATE TABLE public.ds_posts (
    id bigint DEFAULT nextval('public.ds_posts_seq'::regclass) NOT NULL,
    user_id integer DEFAULT 0 NOT NULL,
    blog_date timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    blog_date_gmt timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    blog_content text NOT NULL,
    blog_title text NOT NULL,
    blog_excerpt text NOT NULL,
    blog_status character varying(20) DEFAULT 'publish'::character varying NOT NULL,
    blog_modified timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    blog_modified_gmt timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    guid character varying(255) DEFAULT ''::character varying NOT NULL,
    menu_order integer DEFAULT 0 NOT NULL,
    blog_type character varying(20) DEFAULT 'post'::character varying NOT NULL,
    blog_mime_type character varying(100) DEFAULT ''::character varying NOT NULL,
    CONSTRAINT ds_posts_id_check CHECK ((id > 0)),
    CONSTRAINT ds_posts_menu_order_check CHECK ((menu_order > 0)),
    CONSTRAINT ds_posts_user_id_check CHECK ((user_id > 0))
);


ALTER TABLE public.ds_posts OWNER TO postgres;


CREATE SEQUENCE public.ds_projects_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_projects_seq OWNER TO postgres;


CREATE TABLE public.ds_projects (
    id integer DEFAULT nextval('public.ds_projects_seq'::regclass) NOT NULL,
    category_id integer DEFAULT 0 NOT NULL,
    project character varying(255) NOT NULL,
    created_time timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ds_projects OWNER TO postgres;


CREATE SEQUENCE public.ds_projects_categories_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_projects_categories_seq OWNER TO postgres;


CREATE TABLE public.ds_projects_categories (
    id integer DEFAULT nextval('public.ds_projects_categories_seq'::regclass) NOT NULL,
    category character varying(255) NOT NULL,
    created_time timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ds_projects_categories OWNER TO postgres;


CREATE SEQUENCE public.ds_reports_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_reports_seq OWNER TO postgres;


CREATE TABLE public.ds_reports (
    id integer DEFAULT nextval('public.ds_reports_seq'::regclass) NOT NULL,
    category_id integer DEFAULT 0 NOT NULL,
    report character varying(255) NOT NULL,
    created_time timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ds_reports OWNER TO postgres;


CREATE SEQUENCE public.ds_reports_categories_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_reports_categories_seq OWNER TO postgres;


CREATE TABLE public.ds_reports_categories (
    id integer DEFAULT nextval('public.ds_reports_categories_seq'::regclass) NOT NULL,
    category character varying(255) NOT NULL,
    created_time timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ds_reports_categories OWNER TO postgres;


CREATE SEQUENCE public.ds_topics_categories_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_topics_categories_seq OWNER TO postgres;


CREATE TABLE public.ds_topics_categories (
    id integer DEFAULT nextval('public.ds_topics_categories_seq'::regclass) NOT NULL,
    topicname character varying(255) NOT NULL,
    created_time timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ds_topics_categories OWNER TO postgres;


CREATE SEQUENCE public.ds_topics_categories_main_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_topics_categories_main_seq OWNER TO postgres;


CREATE TABLE public.ds_topics_categories_main (
    id integer DEFAULT nextval('public.ds_topics_categories_main_seq'::regclass) NOT NULL,
    topicname character varying(255) NOT NULL,
    created_time timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ds_topics_categories_main OWNER TO postgres;


CREATE SEQUENCE public.ds_topics_categories_sub_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_topics_categories_sub_seq OWNER TO postgres;


CREATE TABLE public.ds_topics_categories_sub (
    id integer DEFAULT nextval('public.ds_topics_categories_sub_seq'::regclass) NOT NULL,
    topic_id integer DEFAULT 0 NOT NULL,
    category character varying(255) NOT NULL,
    created_time timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ds_topics_categories_sub OWNER TO postgres;


CREATE SEQUENCE public.ds_training_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_training_seq OWNER TO postgres;


CREATE TABLE public.ds_training (
    id integer DEFAULT nextval('public.ds_training_seq'::regclass) NOT NULL,
    category_id integer DEFAULT 0 NOT NULL,
    training character varying(255) NOT NULL,
    created_time timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ds_training OWNER TO postgres;


CREATE SEQUENCE public.ds_training_categories_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_training_categories_seq OWNER TO postgres;


CREATE TABLE public.ds_training_categories (
    id integer DEFAULT nextval('public.ds_training_categories_seq'::regclass) NOT NULL,
    category character varying(255) NOT NULL,
    created_time timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.ds_training_categories OWNER TO postgres;


CREATE SEQUENCE public.ds_user_conversations_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_user_conversations_seq OWNER TO postgres;


CREATE TABLE public.ds_user_conversations (
    message_id integer DEFAULT nextval('public.ds_user_conversations_seq'::regclass) NOT NULL,
    user_id_from integer DEFAULT 0 NOT NULL,
    user_id_to integer DEFAULT 0 NOT NULL,
    date_time timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    priority integer DEFAULT 0 NOT NULL,
    subject character varying(255) DEFAULT ''::character varying NOT NULL,
    message text NOT NULL,
    CONSTRAINT ds_user_conversations_message_id_check CHECK ((message_id > 0)),
    CONSTRAINT ds_user_conversations_priority_check CHECK ((priority > 0)),
    CONSTRAINT ds_user_conversations_user_id_from_check CHECK ((user_id_from > 0)),
    CONSTRAINT ds_user_conversations_user_id_to_check CHECK ((user_id_to > 0))
);


ALTER TABLE public.ds_user_conversations OWNER TO postgres;


CREATE SEQUENCE public.ds_user_profiles_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_user_profiles_seq OWNER TO postgres;


CREATE TABLE public.ds_user_profiles (
    id integer DEFAULT nextval('public.ds_user_profiles_seq'::regclass) NOT NULL,
    user_id integer DEFAULT 0 NOT NULL,
    region character varying(255) NOT NULL,
    profession character varying(255) NOT NULL,
    referred character varying(255) NOT NULL,
    profile_status character varying(20) DEFAULT 'active'::character varying NOT NULL,
    last_visited timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT ds_user_profiles_id_check CHECK ((id > 0)),
    CONSTRAINT ds_user_profiles_user_id_check CHECK ((user_id > 0))
);


ALTER TABLE public.ds_user_profiles OWNER TO postgres;


CREATE SEQUENCE public.ds_users_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ds_users_seq OWNER TO postgres;


CREATE TABLE public.ds_users (
    id integer DEFAULT nextval('public.ds_users_seq'::regclass) NOT NULL,
    customtitle character varying(100) DEFAULT ''::character varying NOT NULL,
    name character varying(400) DEFAULT ''::character varying NOT NULL,
    username character varying(150) DEFAULT ''::character varying NOT NULL,
    email character varying(100) DEFAULT ''::character varying NOT NULL,
    password character varying(100) DEFAULT ''::character varying NOT NULL,
    block smallint DEFAULT 0 NOT NULL,
    sendemail smallint DEFAULT 0,
    registerdate timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    lastvisitdate timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    activation character varying(100) DEFAULT ''::character varying NOT NULL,
    params text NOT NULL,
    lastresettime timestamp(0) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    resetcount integer DEFAULT 0 NOT NULL,
    otpkey character varying(1000) DEFAULT ''::character varying NOT NULL,
    otep character varying(1000) DEFAULT ''::character varying NOT NULL,
    requirereset smallint DEFAULT 0 NOT NULL,
    CONSTRAINT ds_users_block_check CHECK ((block > 0)),
    CONSTRAINT ds_users_id_check CHECK ((id > 0)),
    CONSTRAINT ds_users_requirereset_check CHECK ((requirereset > 0)),
    CONSTRAINT ds_users_sendemail_check CHECK ((sendemail > 0))
);


ALTER TABLE public.ds_users OWNER TO postgres;


COPY public.cms_messages (message_id, full_name, email, message, module, date_sent, date_responded, status, locked) FROM stdin;
\.



COPY public.ds_applications (id, category_id, application, created_time) FROM stdin;
1	1	Policy Implementation	2020-06-08 23:27:12
2	1	Predictive Analytics	2020-06-08 23:27:12
3	1	Behavioral Analytics	2020-06-08 23:27:12
4	1	Smart Cities	2020-06-08 23:27:12
5	2	Fault Detection	2020-06-08 23:27:13
6	2	Intelligent Assistants	2020-06-08 23:27:13
7	2	Network Analysis	2020-06-08 23:27:13
8	3	Climate Analysis	2020-06-08 23:27:13
9	3	Satellite Image Analysis	2020-06-08 23:27:13
10	4	Soil Classification	2020-06-08 23:27:13
11	4	Cross Validation	2020-06-08 23:27:13
12	5	Clinical Studies	2020-06-08 23:27:13
13	5	Diagnosis	2020-06-08 23:27:13
14	5	Disease Prevelance	2020-06-08 23:27:13
15	5	Prescribing Behavior	2020-06-08 23:27:13
16	5	Precision Medicine	2020-06-08 23:27:13
17	6	Data Journalism	2020-06-08 23:27:13
18	6	Advertising	2020-06-08 23:27:13
19	7	Smart Maintenance	2020-06-08 23:27:13
20	7	Biotechnology	2020-06-08 23:27:13
21	8	Blockchain	2020-06-08 23:27:13
22	8	Intrusion Detection and Prevention	2020-06-08 23:27:13
\.



COPY public.ds_applications_categories (id, category, created_time) FROM stdin;
1	Governance	2020-06-08 23:21:14
2	Software Aplications	2020-06-08 23:21:14
3	Geographic Information Systems	2020-06-08 23:21:14
4	Biology	2020-06-08 23:21:14
5	Medicine	2020-06-08 23:21:14
6	Media	2020-06-08 23:21:14
7	Industry	2020-06-08 23:21:14
8	Cybersecurity	2020-06-08 23:21:14
\.



COPY public.ds_books (id, title, description) FROM stdin;
\.



COPY public.ds_books_pages (id, bookid, content) FROM stdin;
\.



COPY public.ds_business_listings (id, author_id, url, contact_info, description, submissiondate) FROM stdin;
\.



COPY public.ds_emergingtopics (id, topicname, created_time) FROM stdin;
1	Streaming Media Analysis	2020-06-08 19:49:07
2	Hybrid Enterprise Architectures	2020-06-08 19:49:07
3	Behavioral Analysis	2020-06-08 19:49:07
4	Network Analysis	2020-06-08 19:49:07
5	Dynamic Analysis	2020-06-08 19:49:07
6	Big Data Architecture	2020-06-08 19:49:08
\.



COPY public.ds_goals (id, creator_id, goal, submissiondate, startdate, enddate) FROM stdin;
\.



COPY public.ds_organizations (id, organization_name, organization_url, organization_description, submissiondate) FROM stdin;
\.



COPY public.ds_posts (id, user_id, blog_date, blog_date_gmt, blog_content, blog_title, blog_excerpt, blog_status, blog_modified, blog_modified_gmt, guid, menu_order, blog_type, blog_mime_type) FROM stdin;
\.



COPY public.ds_projects (id, category_id, project, created_time) FROM stdin;
1	1	Combining Data from Multiple Sources	2020-06-08 22:32:52
2	1	Developing Automated Workflows	2020-06-08 22:32:52
3	2	Developing Prediction Models	2020-06-08 22:32:52
4	2	Statistical Tools	2020-06-08 22:32:52
5	3	ETL	2020-06-08 22:32:52
6	3	Query Design	2020-06-08 22:32:52
7	4	Continuous Integration	2020-06-08 22:32:52
8	4	Continuous Development	2020-06-08 22:32:52
9	5	Classification	2020-06-08 22:32:52
10	5	Clustering	2020-06-08 22:32:52
11	6	Classification Algorithms	2020-06-08 22:32:52
12	6	Text Mining	2020-06-08 22:32:52
13	7	Semantic Extraction	2020-06-08 22:32:53
14	7	Text Representation	2020-06-08 22:32:53
15	8	Problem Solving	2020-06-08 22:32:53
16	8	Communication	2020-06-08 22:32:53
\.



COPY public.ds_projects_categories (id, category, created_time) FROM stdin;
1	Data Integration	2020-06-08 22:28:11
2	Machine Learning	2020-06-08 22:28:11
3	Systems Migration	2020-06-08 22:28:11
4	Application Programming Interfaces	2020-06-08 22:28:11
5	Training Models	2020-06-08 22:28:11
6	Natural Language Processing	2020-06-08 22:28:11
7	Sentiment Analysis	2020-06-08 22:28:11
8	Analytical Tools	2020-06-08 22:28:11
\.



COPY public.ds_reports (id, category_id, report, created_time) FROM stdin;
1	1	Deep Learning in the Semantic Web	2020-06-08 23:41:20
2	1	Privacy and Artificial Intelligence	2020-06-08 23:41:20
3	1	Ethical Data Sharing	2020-06-08 23:41:20
4	1	Data Auditing	2020-06-08 23:41:21
5	2	Large Datasets	2020-06-08 23:41:21
6	2	Data Integration	2020-06-08 23:41:21
7	2	Streaming Data	2020-06-08 23:41:21
8	2	Unstructured Data	2020-06-08 23:41:21
9	3	Knowledge Discovery	2020-06-08 23:41:21
10	3	Business Analytics	2020-06-08 23:41:21
11	3	Performance Measures	2020-06-08 23:41:21
12	3	Dashboards and Visualizations	2020-06-08 23:41:21
13	4	Data Mining	2020-06-08 23:41:21
14	4	Data Aggregation	2020-06-08 23:41:21
15	4	Value Chain Models	2020-06-08 23:41:21
16	4	Enterprise Resource Planning	2020-06-08 23:41:21
17	5	Water Quality	2020-06-08 23:41:21
18	5	Climate Change	2020-06-08 23:41:21
19	5	Environlental Systems	2020-06-08 23:41:21
20	5	Sustainability	2020-06-08 23:41:21
21	6	Diagnosis	2020-06-08 23:41:21
22	6	Disease Prevention and Treatment	2020-06-08 23:41:21
23	6	Personalized Medicine	2020-06-08 23:41:21
24	6	Predictive and Prescriptive Analytics	2020-06-08 23:41:22
25	6	Patient Monitoring	2020-06-08 23:41:22
26	6	Human Genetics	2020-06-08 23:41:22
27	7	Digital Museums	2020-06-08 23:41:22
28	7	Government Policy Making	2020-06-08 23:41:22
29	7	Ontologies and Taxonomies	2020-06-08 23:41:22
30	8	Adaptive Systems	2020-06-08 23:41:22
31	8	Data Analysis Technology Frameworks	2020-06-08 23:41:22
32	8	Cybersecurity	2020-06-08 23:41:22
33	9	Theories	2020-06-08 23:41:22
34	9	Practical Applications	2020-06-08 23:41:22
35	9	Technology Tools	2020-06-08 23:41:22
\.



COPY public.ds_reports_categories (id, category, created_time) FROM stdin;
1	Classification of Documents	2020-06-08 23:33:40
2	Big Data	2020-06-08 23:33:40
3	Knowledge Management	2020-06-08 23:33:40
4	Data Analysis Planning	2020-06-08 23:33:40
5	Ecological Studies	2020-06-08 23:33:40
6	Health Studies	2020-06-08 23:33:40
7	Sociological Studies	2020-06-08 23:33:40
8	Technology	2020-06-08 23:33:41
9	Data Science Training	2020-06-08 23:33:41
10	Additional Topics	2020-06-08 23:33:41
\.



COPY public.ds_topics_categories (id, topicname, created_time) FROM stdin;
1	Big Data	2020-06-08 20:05:04
2	Big Data Analytics	2020-06-08 20:05:04
3	Machine Learning	2020-06-08 20:05:04
4	Business Intelligence	2020-06-08 20:05:04
5	Internet of Things	2020-06-08 20:05:04
6	Data Science	2020-06-08 20:05:04
\.



COPY public.ds_topics_categories_main (id, topicname, created_time) FROM stdin;
1	II Data School	2020-06-08 20:05:17
2	Research	2020-06-08 20:05:17
3	Training	2020-06-08 20:05:17
4	Statistical Modelling	2020-06-08 20:05:17
5	Qualitative Modelling	2020-06-08 20:05:17
6	Analysis Engineering	2020-06-08 20:05:17
7	Data Structures	2020-06-08 20:05:17
8	Analytical Tools	2020-06-08 20:05:17
9	Data Visualization	2020-06-08 20:05:17
10	Emerging Tools	2020-06-08 20:05:17
\.



COPY public.ds_topics_categories_sub (id, topic_id, category, created_time) FROM stdin;
1	1	Research	2020-06-08 20:17:40
2	1	Training	2020-06-08 20:17:40
3	1	Statistical Modelling	2020-06-08 20:17:40
4	1	Qualitative Modelling	2020-06-08 20:17:41
5	2	Neural Networks	2020-06-08 20:17:47
6	2	Cyber Physical Systems	2020-06-08 20:17:47
7	2	Machine Learning Algorithms	2020-06-08 20:17:47
8	2	Dynamic Workflow Automation	2020-06-08 20:17:47
9	3	Management	2020-06-08 20:17:53
10	3	Data Analytical Systems	2020-06-08 20:17:53
11	3	Data Security	2020-06-08 20:17:53
12	3	Analytics	2020-06-08 20:17:53
13	4	Experiments	2020-06-08 20:17:58
14	4	Simulations	2020-06-08 20:17:58
15	4	Models	2020-06-08 20:17:58
16	4	Statistical Relationships	2020-06-08 20:17:59
17	5	Themes	2020-06-08 20:18:04
18	5	Theories	2020-06-08 20:18:04
19	5	Phenomena	2020-06-08 20:18:04
20	5	Studies	2020-06-08 20:18:04
21	6	Data Management	2020-06-08 20:18:11
22	6	Data Structures	2020-06-08 20:18:11
23	6	Data Queries	2020-06-08 20:18:11
24	6	Models	2020-06-08 20:18:11
25	6	Analysis Implementation	2020-06-08 20:18:11
26	7	Unstructured	2020-06-08 20:18:16
27	7	Structured	2020-06-08 20:18:16
28	8	Scientific Models	2020-06-08 20:18:22
29	8	Statistics	2020-06-08 20:18:22
30	8	Representations	2020-06-08 20:18:22
31	8	Theme Analysis	2020-06-08 20:18:22
32	8	Visualization	2020-06-08 20:18:22
33	9	Charts	2020-06-08 20:18:27
34	9	Graphs	2020-06-08 20:18:27
35	10	Machine Learning	2020-06-08 20:18:33
36	10	Ensembles	2020-06-08 20:18:33
37	10	Graph Analytics	2020-06-08 20:18:33
38	10	Deep Learning	2020-06-08 20:18:33
39	10	Natural Language Processing	2020-06-08 20:18:33
\.



COPY public.ds_training (id, category_id, training, created_time) FROM stdin;
1	1	Entrepreneurial Data Ecosystems	2020-06-08 23:14:36
2	1	Forecasting and Predictive Analysis	2020-06-08 23:14:36
3	2	Educational and Industrial Cooperation	2020-06-08 23:14:36
4	3	Professional Development Training	2020-06-08 23:14:36
5	3	Risk Management	2020-06-08 23:14:36
6	4	Strategic Business Processes	2020-06-08 23:14:36
7	4	Learning Culture	2020-06-08 23:14:36
8	5	Supervised	2020-06-08 23:14:36
9	5	Unsupervised	2020-06-08 23:14:36
10	5	Semi Supervised	2020-06-08 23:14:36
11	6	Evolutionary	2020-06-08 23:14:37
12	6	Deep Learning	2020-06-08 23:14:37
13	7	Classification	2020-06-08 23:14:37
14	7	Regression	2020-06-08 23:14:37
15	8	Clustering	2020-06-08 23:14:37
\.



COPY public.ds_training_categories (id, category, created_time) FROM stdin;
1	Entrepreneurial Data Science	2020-06-08 23:08:42
2	Data Science Education	2020-06-08 23:08:42
3	Data Science Standards	2020-06-08 23:08:43
4	Knowledge Management	2020-06-08 23:08:43
5	Machine Learning	2020-06-08 23:08:43
6	Machine Learning	2020-06-08 23:08:43
7	Supervised Learning	2020-06-08 23:08:43
8	Unsupervised Learning	2020-06-08 23:08:43
\.



COPY public.ds_user_conversations (message_id, user_id_from, user_id_to, date_time, priority, subject, message) FROM stdin;
\.



COPY public.ds_user_profiles (id, user_id, region, profession, referred, profile_status, last_visited) FROM stdin;
\.



COPY public.ds_users (id, customtitle, name, username, email, password, block, sendemail, registerdate, lastvisitdate, activation, params, lastresettime, resetcount, otpkey, otep, requirereset) FROM stdin;
\.



SELECT pg_catalog.setval('public.cms_messages_seq', 1, false);



SELECT pg_catalog.setval('public.ds_applications_categories_seq', 9, false);



SELECT pg_catalog.setval('public.ds_applications_seq', 23, false);



SELECT pg_catalog.setval('public.ds_books_pages_seq', 1, false);



SELECT pg_catalog.setval('public.ds_books_seq', 1, false);



SELECT pg_catalog.setval('public.ds_business_listings_seq', 1, false);



SELECT pg_catalog.setval('public.ds_emergingtopics_seq', 7, false);



SELECT pg_catalog.setval('public.ds_goals_seq', 1, false);



SELECT pg_catalog.setval('public.ds_organizations_seq', 1, false);



SELECT pg_catalog.setval('public.ds_posts_seq', 1, false);



SELECT pg_catalog.setval('public.ds_projects_categories_seq', 9, false);



SELECT pg_catalog.setval('public.ds_projects_seq', 17, false);



SELECT pg_catalog.setval('public.ds_reports_categories_seq', 11, false);



SELECT pg_catalog.setval('public.ds_reports_seq', 36, false);



SELECT pg_catalog.setval('public.ds_topics_categories_main_seq', 11, false);



SELECT pg_catalog.setval('public.ds_topics_categories_seq', 7, false);



SELECT pg_catalog.setval('public.ds_topics_categories_sub_seq', 40, false);



SELECT pg_catalog.setval('public.ds_training_categories_seq', 9, false);



SELECT pg_catalog.setval('public.ds_training_seq', 16, false);



SELECT pg_catalog.setval('public.ds_user_conversations_seq', 1, false);



SELECT pg_catalog.setval('public.ds_user_profiles_seq', 1, false);


SELECT pg_catalog.setval('public.ds_users_seq', 1, false);



ALTER TABLE ONLY public.ds_users
    ADD CONSTRAINT ck_email UNIQUE (email);



ALTER TABLE ONLY public.ds_user_profiles
    ADD CONSTRAINT ck_user_id UNIQUE (user_id);



ALTER TABLE ONLY public.ds_users
    ADD CONSTRAINT ck_username UNIQUE (username);



ALTER TABLE ONLY public.cms_messages
    ADD CONSTRAINT cms_messages_pkey PRIMARY KEY (message_id);


ALTER TABLE ONLY public.ds_applications_categories
    ADD CONSTRAINT ds_applications_categories_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_applications
    ADD CONSTRAINT ds_applications_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_books_pages
    ADD CONSTRAINT ds_books_pages_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_books
    ADD CONSTRAINT ds_books_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_business_listings
    ADD CONSTRAINT ds_business_listings_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_emergingtopics
    ADD CONSTRAINT ds_emergingtopics_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_goals
    ADD CONSTRAINT ds_goals_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_organizations
    ADD CONSTRAINT ds_organizations_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_posts
    ADD CONSTRAINT ds_posts_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_projects_categories
    ADD CONSTRAINT ds_projects_categories_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_projects
    ADD CONSTRAINT ds_projects_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_reports_categories
    ADD CONSTRAINT ds_reports_categories_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_reports
    ADD CONSTRAINT ds_reports_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_topics_categories_main
    ADD CONSTRAINT ds_topics_categories_main_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_topics_categories
    ADD CONSTRAINT ds_topics_categories_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_topics_categories_sub
    ADD CONSTRAINT ds_topics_categories_sub_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_training_categories
    ADD CONSTRAINT ds_training_categories_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_training
    ADD CONSTRAINT ds_training_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_user_conversations
    ADD CONSTRAINT ds_user_conversations_pkey PRIMARY KEY (message_id);


ALTER TABLE ONLY public.ds_user_profiles
    ADD CONSTRAINT ds_user_profiles_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.ds_users
    ADD CONSTRAINT ds_users_pkey PRIMARY KEY (id);


CREATE INDEX author_id ON public.ds_business_listings USING btree (author_id);

CREATE INDEX creator_id ON public.ds_goals USING btree (creator_id);

CREATE INDEX user_id ON public.ds_posts USING btree (user_id);


