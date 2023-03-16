import { CreateParams, DeleteManyParams, DeleteParams, fetchUtils, GetListParams, GetManyParams, GetManyReferenceParams, GetOneParams, UpdateManyParams, UpdateParams } from "react-admin";
/*import { stringify } from "query-admin";*/

const apiUrl = 'http://127.0.0.1:8000';
const httpClient = fetchUtils.fetchJson;

export const myDataProvider = {
    getList: (resource: string, params: GetListParams) => {
        const { page, perPage } = params.pagination;
        const { field, order } = params.sort;
        const query = {
            sort: JSON.stringify([field, order]),
            range: JSON.stringify([(page - 1) * perPage, page * perPage -1]),
            filter: JSON.stringify(params.filter)
        }
        const url = `${apiUrl}/${resource}?${JSON.stringify(query)}`;
        console.log(url);
        return httpClient(url).then(({headers, json}) => ({
            data:json,
            total: parseInt(headers.get("x-total-count")!.split("/").pop() ?? "0"),
        })

        );
    },

    getOne: (resource: string, params: GetOneParams) => {
        
        const url = `${apiUrl}/${resource}/${params.id}`;
        console.log(url);
        return httpClient(url).then(({json}) => ({
            data: json
        })
        
        );
    },

    getMany: (resource: string, params: GetManyParams) => {
        const query = {
            filter: JSON.stringify({ id: params.ids }),
        }
        const url = `${apiUrl}/${resource}?${JSON.stringify(query)}`;
        console.log(url);
        return httpClient(url).then(({json}) => ({
            data: json
        })

        );
    },

    getManyReference: (resource: string, params: GetManyReferenceParams) => {

    },

    update: (resource: string, params: UpdateParams) => {

    },

    updateMany: (resource: string, params: UpdateManyParams) => {

    },

    create: (resource: string, params: CreateParams) => {

    },

    delete: (resource: string, params: DeleteParams) => {

    },

    deleteMany: (resource: string, params: DeleteManyParams) => {

    }
}
